"""Tiny synthetic project inputs for engineering checks.

These values are invented to exercise parsing and invariants. They are not scientific data and
must never be mistaken for Yale inputs.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

K = 25
CONDITIONS = ["Control", "IPF"]
CELL_TYPES = ["AT1", "AT2", "Activated_Fibrotic_FBs", "Proliferating_NK_NKT"]
CHROMLINKER_CONTEXTS = [
    "Control.AT1_niche_1",
    "Control.AT1_niche_2",
    "IPF.AT1_niche_1",
    "IPF.AT1_niche_2",
    "IPF.Activated_Fibrotic_FBs_niche_1",
    "IPF.Activated_Fibrotic_FBs_niche_2",
    "Control.AT2",
]
EXPRESSION_CONTEXTS = [
    *CHROMLINKER_CONTEXTS,
    "Control.Activated_Fibrotic_FBs_niche_1",
    "Control.Activated_Fibrotic_FBs_niche_2",
    "IPF.AT2",
    "Control.Proliferating_NK_NKT",
]
# TF_A is also a target; "NA" is a legitimate-looking symbol that must not become missing.
CHROMLINKER_ROWS = [
    ("TF_A", "GENE1", [0.5, 0.0, 0.25, 0.0, 0.0, 0.1, 0.0]),
    ("TF_A", "TF_B", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
    ("TF_B", "NA", [1.0, 0.3, 0.0, 0.2, 0.4, 0.0, 0.05]),
]
EXPRESSION_GENES = ["TF_A", "TF_B", "GENE1", "NA", "MATR3", "MATR3-1"]
SIGNATURE_GENES = ["TF_A", "TF_B", "GENE1", "SIG_ONLY", "MATR3", "MATR3.1"]
SIGNATURE_CELLS = {
    ("AT1", "Control"): (60, 7),
    ("AT1", "IPF"): (40, 9),
    ("Activated_Fibrotic_FBs", "Control"): (5, 3),
    ("Activated_Fibrotic_FBs", "IPF"): (12, 4),
}
NEIGHBORHOODS = {
    # focal type -> (resolution, categories, niche_1 counts, niche_2 counts)
    "AT1": (0.08, ["AT1", "AT2", "Activated_Fibrotic_FBs", "Proliferating_NK_NKT"], [10, 10, 4, 1], [5, 5, 15, 0]),
    # Proliferating_NK_NKT is deliberately not reported here: it must stay unreported, not zero.
    "Activated_Fibrotic_FBs": (0.1, ["AT1", "AT2", "Activated_Fibrotic_FBs"], [2.5, 2.5, 20], [12.5, 7.5, 5]),
}


def write_delimited(path: Path, header: list[str], rows: list[list[object]], delimiter: str) -> None:
    lines = [delimiter.join(header)] + [delimiter.join(str(value) for value in row) for row in rows]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_synthetic_project(root: Path) -> Path:
    """Write synthetic inputs plus a project config under `root`; return the config path."""
    files = root / "files"
    (files / "Neighbour_celltypes").mkdir(parents=True)
    (root / "pyproject.toml").write_text("[project]\nname = 'synthetic'\n", encoding="utf-8")

    write_delimited(
        files / "chromlinker.csv",
        ["TF", "Gene", *CHROMLINKER_CONTEXTS],
        [[tf, gene, *values] for tf, gene, values in CHROMLINKER_ROWS],
        ",",
    )
    write_delimited(
        files / "pseudobulk.txt",
        ["gene", *EXPRESSION_CONTEXTS],
        [
            [gene, *[float((i * 7 + j) % 5) for j in range(len(EXPRESSION_CONTEXTS))]]
            for i, gene in enumerate(EXPRESSION_GENES)
        ],
        "\t",
    )
    signature_rows = []
    for (cell_type, condition), (n1, n2) in SIGNATURE_CELLS.items():
        for i, gene in enumerate(SIGNATURE_GENES):
            mean1, mean2 = round(0.1 * i, 3), round(0.15 * i + 0.05, 3)
            signature_rows.append(
                [
                    "SYN",
                    cell_type,
                    condition,
                    "niche_2_vs_niche_1",
                    gene,
                    mean1,
                    mean2,
                    repr(mean2 - mean1),
                    0.1 * (i % 3),
                    0.2 * (i % 4),
                    n1,
                    n2,
                    "mean log-normalized expression, Niche 2 minus Niche 1",
                ]
            )
    write_delimited(
        files / "signatures.tsv",
        [
            "dataset",
            "cell_type",
            "condition",
            "comparison",
            "gene",
            "mean_log_normalized_expression_niche_1",
            "mean_log_normalized_expression_niche_2",
            "niche_2_minus_niche_1_mean_log_normalized_expression",
            "pct_expressing_niche_1",
            "pct_expressing_niche_2",
            "n_cells_niche_1",
            "n_cells_niche_2",
            "effect_definition",
        ],
        signature_rows,
        "\t",
    )
    definitions = []
    for focal, (resolution, categories, niche_1, niche_2) in NEIGHBORHOODS.items():
        name = f"{focal}_knn_{K}_res{resolution}_neighbor_mean_counts_by_niche.tsv"
        write_delimited(
            files / "Neighbour_celltypes" / name,
            ["spatial_niche", *categories],
            [["niche_1", *niche_1], ["niche_2", *niche_2]],
            "\t",
        )
        definitions.append(
            {
                "focal_cell_type": focal,
                "neighborhood_path": f"files/Neighbour_celltypes/{name}",
                "delimiter": "\t",
                "niche_column": "spatial_niche",
                "k_neighbors": K,
                "clustering_resolution": resolution,
                "conditions_pooled": CONDITIONS,
                "method": "synthetic_knn_composition",
            }
        )

    config = {
        "schema_version": 1,
        "input_mode": "fixture",
        "data_root": "data",
        "ingest_chunk_rows": 2,
        "dataset": {
            "name": "SYN",
            "species": "Homo sapiens",
            "ncbi_taxon_id": 9606,
            "tissue": "lung",
            "model_system": "primary tissue",
            "conditions": {"Control": {"disease": None}, "IPF": {"disease": "idiopathic pulmonary fibrosis"}},
        },
        "chromlinker": {
            "path": "files/chromlinker.csv",
            "delimiter": ",",
            "tf_column": "TF",
            "target_column": "Gene",
            "score_label": "synthetic_score",
        },
        "expression": {"path": "files/pseudobulk.txt", "delimiter": "\t", "gene_column": "gene", "value_unit": "CPTT"},
        "niche_expression_signatures": {"path": "files/signatures.tsv", "delimiter": "\t"},
        "niche_definitions": definitions,
        "cell_types": {name: {"display_name": name.replace("_", " ")} for name in CELL_TYPES},
        "at1_scope": {"cell_type": "AT1", "tf_seeds": ["TF_A"]},
        "tolerances": {"signature_effect_abs": 1e-8, "signature_effect_rel": 1e-6, "neighborhood_row_sum": 1e-6},
    }
    config_path = root / "configs" / "project.yaml"
    config_path.parent.mkdir()
    config_path.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
    return config_path


@pytest.fixture
def synthetic_project(tmp_path: Path) -> Path:
    return build_synthetic_project(tmp_path)
