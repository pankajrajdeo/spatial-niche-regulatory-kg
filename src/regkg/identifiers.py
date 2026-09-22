"""Species-qualified local gene identities built only from exact source symbols.

P1 resolves no external identifiers. Later mapping enrichment adds HGNC/Ensembl/NCBI fields
without changing `gene_id`, which depends only on species and the exact source symbol.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Mapping

import pandas as pd

from regkg.models import MappingStatus
from regkg.provenance import stable_id

# Both conventions occur in the supplied files: anndata-style "MATR3.1" (signatures) and
# R-style "MATR3-1" (pseudobulk). Whether they denote the same Ensembl feature is not recorded,
# so this is only a diagnostic; symbols are never merged or stripped on this basis.
_SUFFIX_VARIANT = re.compile(r"^(?P<base>.+)[.-](?P<n>\d+)$")

TF_SOURCE_CHROMLINKER = "chromlinker_tf_column"


def normalize_symbol(symbol: str) -> str:
    """Unicode NFC and whitespace trim only; no case folding or suffix stripping."""
    return unicodedata.normalize("NFC", symbol).strip()


def local_gene_id(taxon_id: int, source_symbol: str) -> str:
    return stable_id("gene", {"ncbi_taxon_id": taxon_id, "source_symbol": source_symbol})


def suffix_variant_bases(symbols_by_source: Mapping[str, set[str]]) -> dict[str, str]:
    """Symbols that look like a make-unique copy of another symbol present in the same source."""
    variants: dict[str, str] = {}
    for symbols in symbols_by_source.values():
        for symbol in symbols:
            match = _SUFFIX_VARIANT.match(symbol)
            if match and match["base"] in symbols:
                variants[symbol] = match["base"]
    return variants


def build_gene_table(
    species: str,
    taxon_id: int,
    chromlinker_tfs: set[str],
    chromlinker_targets: set[str],
    expression_genes: set[str],
    signature_genes: set[str],
) -> pd.DataFrame:
    """One record per exact source symbol across every source; nothing is inner-joined away."""
    symbols = sorted(chromlinker_tfs | chromlinker_targets | expression_genes | signature_genes)
    normalized = {symbol: normalize_symbol(symbol) for symbol in symbols}
    collisions = pd.Series(normalized).loc[lambda s: s.duplicated(keep=False)]
    if not collisions.empty:
        raise ValueError(f"distinct source symbols collide after normalization: {collisions.to_dict()}")
    variants = suffix_variant_bases(
        {
            "chromlinker": chromlinker_tfs | chromlinker_targets,
            "expression": expression_genes,
            "signatures": signature_genes,
        }
    )
    is_tf = [True if symbol in chromlinker_tfs else None for symbol in symbols]
    return pd.DataFrame(
        {
            "gene_id": [local_gene_id(taxon_id, symbol) for symbol in symbols],
            "species": species,
            "ncbi_taxon_id": taxon_id,
            "source_symbol": symbols,
            "normalized_symbol": [normalized[symbol] for symbol in symbols],
            "approved_symbol": None,
            "hgnc_id": None,
            "ensembl_gene_id": None,
            "ncbi_gene_id": None,
            "mapping_status": MappingStatus.UNRESOLVED_EXTERNAL_ID.value,
            "mapping_source": None,
            "mapping_version": None,
            # TF status is known only where ChromLinker used the symbol as a regulator; elsewhere unknown.
            "is_tf": pd.array(is_tf, dtype="boolean"),
            "is_tf_source": [TF_SOURCE_CHROMLINKER if flag else None for flag in is_tf],
            "in_chromlinker_tf": [symbol in chromlinker_tfs for symbol in symbols],
            "in_chromlinker_target": [symbol in chromlinker_targets for symbol in symbols],
            "in_expression": [symbol in expression_genes for symbol in symbols],
            "in_niche_signatures": [symbol in signature_genes for symbol in symbols],
            "suffix_variant_base_symbol": [variants.get(symbol) for symbol in symbols],
        }
    )
