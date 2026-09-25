"""Selected-provider models, strict structured calls and durable shared accounting."""

from decimal import Decimal
from pathlib import Path

from regkg.config import ModelSpec, validate_service_url
from regkg.provenance import canonical_json, read_json, sha256_text, write_json
from regkg.workflows.screening import Allowance, Budget, _usage


def model_kwargs(spec: ModelSpec, env: dict, settings: dict) -> dict:
    keys = {"litellm": "LITELLM_API_KEY", "openrouter": "OPENROUTER_API_KEY", "groq": "GROQ_API_KEY"}
    if spec.provider not in keys or not env.get(keys[spec.provider]):
        raise ValueError(f"Missing selected-provider credential for {spec.provider}")
    common = dict(
        model=spec.model_name,
        api_key=env[keys[spec.provider]],
        temperature=0,
        max_tokens=settings["max_output_tokens"],
        timeout=settings["timeout_seconds"],
        max_retries=0,
    )
    if spec.provider == "litellm":
        common["base_url"] = validate_service_url("LITELLM_BASE_URL", env.get("LITELLM_BASE_URL", ""))
        if settings.get("reasoning_effort"):
            common["reasoning_effort"] = settings["reasoning_effort"]
    elif spec.provider == "openrouter":
        common["base_url"] = "https://openrouter.ai/api/v1"
        provider = {
            "order": (env.get("OPENROUTER_PROVIDER_ORDER") or "morph,deepinfra,together,baseten,coreweave").split(","),
            "allow_fallbacks": True,
            "require_parameters": True,
        }
        prices = {}
        for name, field in [("OPENROUTER_MAX_PRICE_INPUT", "prompt"), ("OPENROUTER_MAX_PRICE_OUTPUT", "completion")]:
            if env.get(name):
                value = Decimal(env[name])
                if not value.is_finite() or value < 0:
                    raise ValueError(f"Invalid {name}")
                prices[field] = float(value)
        if prices:
            provider["max_price"] = prices
        common["extra_body"] = {
            "provider": provider,
            "reasoning": {"effort": env.get("OPENROUTER_REASONING") or "low"},
            "usage": {"include": True},
        }
    return common


def build_chat_model(spec: ModelSpec, env: dict, settings: dict):
    kwargs = model_kwargs(spec, env, settings)
    try:
        if spec.provider == "groq":
            from langchain_groq import ChatGroq

            return ChatGroq(**kwargs)
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(**kwargs)
    except ImportError as exc:
        raise RuntimeError(f"Install the selected {'chat-groq' if spec.provider == 'groq' else 'chat'} extra") from exc


def token_bound(value) -> int:
    # UTF-8 byte count is deliberately conservative; no claim of exact GLM tokenization.
    return len(canonical_json(value).encode("utf-8")) + 512


def raw_record(message) -> dict:
    return {
        "content": message.content,
        "tool_calls": getattr(message, "tool_calls", []),
        "usage": _usage(message),
        "model_name": message.response_metadata.get("model_name"),
        "finish_reason": message.response_metadata.get("finish_reason"),
    }


class Runtime:
    def __init__(self, directory: Path, settings: dict, identity: dict, retry_failed=False, budget_path=None):
        self.directory, self.settings, self.identity = directory, settings, identity
        self.retry_failed = retry_failed
        directory.mkdir(parents=True, exist_ok=True)
        self.budget = Budget(
            Allowance(
                settings["max_calls"],
                settings["max_input_tokens_total"],
                settings["max_output_tokens_total"],
                settings["max_usd"],
            ),
            budget_path or directory / "budget.json",
        )

    def structured(self, model, schema, system: str, payload: dict, role: str) -> dict:
        from langchain_core.messages import HumanMessage, SystemMessage

        identity = {
            "runtime": self.identity,
            "role": role,
            "schema": schema.model_json_schema(),
            "system": system,
            "payload": payload,
        }
        key = sha256_text(canonical_json(identity))
        path = self.directory / "calls" / f"{key}.json"
        attempts = []
        if path.exists():
            record = read_json(path)
            if record["status"] == "SUCCEEDED":
                schema.model_validate(record["parsed"])
                return {**record, "cached": True}
            if not self.retry_failed or record["status"] == "IN_FLIGHT_UNKNOWN":
                # Unknown interrupted dispatches require reconciliation, not a free retry.
                return {**record, "cached": True}
            attempts = record.get("attempts", [])
        bound = token_bound({"system": system, "payload": payload, "schema": schema.model_json_schema()})
        if bound > self.settings["max_input_tokens"]:
            return {"status": "INPUT_LIMIT", "input_token_bound": bound, "parsed": None, "cached": False}
        # Supply Pydantic-derived JSON Schema so SDK parsing cannot discard an invalid
        # response before raw text/usage are retained. Host Pydantic validation stays strict.
        runnable = model.with_structured_output(
            schema.model_json_schema(), method=self.settings["structured_method"], include_raw=True, strict=True
        )
        messages = [SystemMessage(content=system), HumanMessage(content=canonical_json(payload))]
        for _ in range(self.settings["attempts_per_call"]):
            reservation, stop = self.budget.reserve(bound, self.settings["max_output_tokens"])
            if stop:
                return {"status": f"LIMIT:{stop}", "parsed": None, "cached": False}
            write_json(
                path,
                {
                    "status": "IN_FLIGHT_UNKNOWN",
                    "parsed": None,
                    "input_sha256": key,
                    "attempts": attempts,
                    "reserved": reservation,
                },
            )
            try:
                result = runnable.invoke(messages, config={"callbacks": []})
                raw = raw_record(result["raw"])
                self.budget.settle(reservation, raw["usage"])
                attempts.append(raw)
                if result.get("parsed") is not None and not result.get("parsing_error"):
                    parsed = schema.model_validate(result["parsed"]).model_dump()
                    record = {
                        "status": "SUCCEEDED",
                        "parsed": parsed,
                        "input_sha256": key,
                        "attempts": attempts,
                        "cached": False,
                    }
                    write_json(path, record)
                    return record
            except Exception as exc:
                error = {"error_type": type(exc).__name__}
                if hasattr(exc, "errors"):
                    error["validation_issues"] = [
                        {"location": list(item["loc"]), "type": item["type"]}
                        for item in exc.errors(include_input=False, include_context=False)
                    ]
                attempts.append(error)
                # Unknown timeout/network usage remains conservatively reserved.
        record = {"status": "FAILED", "parsed": None, "input_sha256": key, "attempts": attempts, "cached": False}
        write_json(path, record)
        return record
