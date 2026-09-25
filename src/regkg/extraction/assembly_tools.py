"""Six bounded tools over a host-pinned publication; no network, paths or execution."""

from decimal import Decimal, InvalidOperation
from threading import Lock

from pydantic import ValidationError

from regkg.extraction import assembly_schemas as schemas
from regkg.provenance import canonical_json, sha256_text

ARGS = {
    "list_assets": schemas.PageArgs,
    "search_content": schemas.SearchArgs,
    "read_passages": schemas.ReadArgs,
    "inspect_table": schemas.InspectArgs,
    "read_table_rows": schemas.TableArgs,
    "resolve_reference": schemas.ReferenceArgs,
}


class SourceTools:
    def __init__(self, registry, bundle, anchors, max_chars=6000, meaning_reviews=None):
        self.registry, self.bundle, self.max_chars = registry, bundle, max_chars
        self.parts = {p["part_id"]: p for p in registry.paper_parts(bundle)}
        self.seen = {p["part_id"] for p in anchors}
        self.cursors, self.requests = {}, {}
        self.lock = Lock()
        self.nonproductive = 0
        self.meaning_reviews = meaning_reviews or {}

    def envelope(self, status="OK", data=None, parts=None, next_cursor=None, available=None, warnings=None):
        parts, data = parts or [], data or []
        return {
            "schema_version": "assembly-tool-1",
            "status": status,
            "data": data,
            "parts": parts,
            "next_cursor": next_cursor,
            "coverage": {"returned": len(data) or len(parts), "available": available, "partial": bool(next_cursor)},
            "warnings": warnings or [],
        }

    def page(self, records, args, key, include_parts=False):
        cursor = args.get("cursor")
        if cursor and (cursor not in self.cursors or self.cursors[cursor][0] != key):
            return self.envelope("INVALID_ARGUMENT")
        start = self.cursors[cursor][1] if cursor else 0
        chosen = []
        for record in records[start : start + args["limit"]]:
            trial = self.envelope(
                parts=chosen + [record] if include_parts else [],
                data=[] if include_parts else chosen + [record],
                available=len(records),
            )
            if len(canonical_json(trial)) + 128 > self.max_chars:
                break
            chosen.append(record)
        if not chosen and start < len(records):
            return self.envelope(
                "LIMIT_REACHED",
                warnings=[{"code": "CONTEXT_TOO_LARGE", "message": "A required source part cannot fit."}],
            )
        stop = start + len(chosen)
        nxt = sha256_text(f"{key}:{stop}") if stop < len(records) else None
        if nxt:
            self.cursors[nxt] = (key, stop)
        return self.envelope(
            parts=chosen if include_parts else [],
            data=[] if include_parts else chosen,
            next_cursor=nxt,
            available=len(records),
        )

    def call(self, name, **raw):
        with self.lock:
            try:
                args = ARGS[name].model_validate(raw).model_dump()
            except (KeyError, ValidationError):
                return self.envelope("INVALID_ARGUMENT")
            # Recheck source hash even on identical cached tool requests.
            try:
                self.registry.document(self.bundle["document_id"])
            except ValueError:
                return self.envelope("SOURCE_CHANGED")
            key = sha256_text(
                canonical_json(
                    {
                        "name": name,
                        "args": {k: v for k, v in args.items() if k != "cursor"},
                        "source": self.bundle["canonical_sha256"],
                    }
                )
            )
            request_key = sha256_text(canonical_json([name, args]))
            if request_key in self.requests:
                self.nonproductive += 1
                return self.requests[request_key]
            result = self._dispatch(name, args, key)
            if len(canonical_json(result)) > self.max_chars:
                result = self.envelope("LIMIT_REACHED")
            new = {p["part_id"] for p in result["parts"]} - self.seen
            self.seen.update(new)
            self.nonproductive = 0 if new or result["data"] else self.nonproductive + 1
            if len(canonical_json(result)) > self.max_chars:
                result = self.envelope("LIMIT_REACHED")
            self.requests[request_key] = result
            return result

    def _dispatch(self, name, args, key):
        parts = list(self.parts.values())
        asset = self.bundle["source_asset_sha256"]
        if name == "list_assets":
            return self.page(
                [
                    {
                        "asset_id": asset,
                        "role": "canonical_article",
                        "format": self.bundle["text_version"],
                        "version_id": self.bundle["text_version"],
                        "parse_state": self.bundle["document_parse"]["state"],
                        "document_ids": [self.bundle["document_id"]],
                    }
                ],
                args,
                key,
            )
        if name == "read_passages":
            if any(i not in self.parts for i in args["part_ids"]):
                return self.envelope("DENIED")
            return self.envelope(parts=[self.parts[i] for i in args["part_ids"]])
        if name == "search_content":
            if args["asset_ids"] and set(args["asset_ids"]) != {asset}:
                return self.envelope("DENIED")
            from regkg.literature.retrieval import tokenize

            terms = set(tokenize(args["query"]))
            scored = [
                (len(terms & set(tokenize(p["text"]))), p)
                for p in parts
                if not args["kinds"] or p["kind"] in args["kinds"]
            ]
            found = [p for score, p in sorted(scored, key=lambda x: (-x[0], x[1]["order"])) if score]
            return self.page(found, args, key, True)
        if name == "inspect_table":
            if args["asset_id"] != asset:
                return self.envelope("DENIED")
            tables = sorted({p["table_id"] for p in parts if p.get("table_id")})
            data = []
            for tid in tables:
                if args["table_id"] and args["table_id"] != tid:
                    continue
                rows = [p for p in parts if p.get("table_id") == tid]
                data.append(
                    {
                        "table_id": tid,
                        "row_count": sum(p["kind"] == "table_row" for p in rows),
                        "columns": sorted({str(c["col_start"]) for p in rows for c in p.get("cells") or []}),
                        "header_part_ids": [p["part_id"] for p in rows if p["kind"] == "table_header"],
                        "legend_part_ids": [
                            p["part_id"] for p in rows if p["kind"] in {"table_caption", "table_footnote"}
                        ],
                        "meaning_review_state": "REVIEWED" if tid in self.meaning_reviews else "UNKNOWN",
                    }
                )
            return self.page(data, args, key)
        if name == "read_table_rows":
            rows = [p for p in parts if p.get("table_id") == args["table_id"] and p["kind"] == "table_row"]
            columns = {str(c["col_start"]) for p in rows for c in p.get("cells") or []}
            if not set(args["column_ids"]) <= columns:
                return self.envelope("INVALID_ARGUMENT")
            if args["row_ids"] is not None:
                if not set(args["row_ids"]) <= {p["part_id"] for p in rows}:
                    return self.envelope("DENIED")
                rows = [p for p in rows if p["part_id"] in args["row_ids"]]
            for f in args["filters"]:
                if f["column_id"] not in columns:
                    return self.envelope("INVALID_ARGUMENT")
                numeric = f["op"] in {"lt", "le", "gt", "ge"}
                reviewed = self.meaning_reviews.get(args["table_id"], {}).get(f["column_id"], {})
                if numeric and not (reviewed.get("numeric") and reviewed.get("units") and reviewed.get("scale")):
                    return self.envelope(
                        "UNSUPPORTED",
                        warnings=[{"code": "UNREVIEWED_NUMERIC_MEANING", "message": "No numeric filtering."}],
                    )
                kept = []
                for p in rows:
                    values = [str(c["text"]) for c in p.get("cells") or [] if str(c["col_start"]) == f["column_id"]]
                    if len(values) != 1:
                        continue
                    value = values[0]
                    if numeric:
                        try:
                            a, b = Decimal(value), Decimal(f["values"][0])
                            if not a.is_finite() or not b.is_finite():
                                return self.envelope("UNSUPPORTED")
                            match = {"lt": a < b, "le": a <= b, "gt": a > b, "ge": a >= b}[f["op"]]
                        except InvalidOperation:
                            return self.envelope("UNSUPPORTED")
                    else:
                        match = f["values"][0] in value if f["op"] == "contains_literal" else value in f["values"]
                    if match:
                        kept.append(p)
                rows = kept
            # Original whole rows preserve headers and never hide a conflicting unselected cell.
            return self.page(rows, args, key, True)
        if name == "resolve_reference":
            origin = self.parts.get(args["from_part_id"])
            if not origin or origin["part_id"] not in self.seen:
                return self.envelope("DENIED")
            label = args["reference_label"]
            if label.casefold() not in origin["text"].casefold():
                return self.envelope("NOT_FOUND")
            targets = [
                p
                for p in parts
                if p["part_id"] != origin["part_id"]
                and p.get("item_label")
                and p["item_label"].casefold().rstrip(".") == label.casefold().rstrip(".")
            ]
            response = self.page(targets, {"cursor": None, "limit": args["limit"]}, key, True)
            # A label match is a navigation hint, not proof of experimental equivalence.
            response["status"] = "AMBIGUOUS" if targets else "NOT_FOUND"
            response["warnings"] = [
                {"code": "LABEL_MATCH_ONLY", "message": "Experiment linkage requires source validation."}
            ]
            return response
        return self.envelope("INVALID_ARGUMENT")

    def langchain_tools(self):
        from langchain_core.tools import StructuredTool

        tools = []
        for name, schema in ARGS.items():

            def invoke(_name=name, **kwargs):
                return self.call(_name, **kwargs)

            tools.append(
                StructuredTool.from_function(
                    invoke,
                    name=name,
                    args_schema=schema,
                    description=f"Read frozen local source through {name}; no external access or inference.",
                )
            )
        return tools
