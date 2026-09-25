"""Synthetic contract checks; not biomedical accuracy estimates."""

from pathlib import Path

import pytest

from regkg.extraction.grounded import (
    REVIEW_FIELDS,
    FieldCheck,
    Mention,
    Observation,
    ObservationReview,
    SourceFact,
    SourceRead,
    contracts,
    load_scientific_schema,
    observation_failures,
    review_finding,
    system_prompt,
    unpack_verification,
    validate_mentions,
    verification_contract,
)
from regkg.extraction.schemas import Citation


def source(text):
    return {
        "part_id": "p:1",
        "text": text,
        "start": 10,
        "document_id": "d:1",
        "document_sha256": "synthetic",
        "asset_sha256": "synthetic",
    }


@pytest.fixture
def policy():
    return load_scientific_schema(Path("configs/extraction_schema.yaml"))


def test_yaml_controls_model_enum_and_group_preservation(policy):
    schema, _ = contracts(policy)
    assert set(schema.model_json_schema()["$defs"]["TypedMention"]["properties"]["kind"]["enum"]) == set(
        policy.entity_types
    )
    part = source("Joint deletion of GeneA and GeneB increased TypeC cells.")
    item = Mention(
        surface="GeneA and GeneB",
        kind="gene_group",
        part_id=part["part_id"],
        anchor=part["text"],
        species=None,
        species_evidence=None,
    )
    good, rejected = validate_mentions([item], [part], policy, {})
    assert not rejected and len(good) == 1
    assert good[0]["start"] == 28 and good[0]["kind"] == "gene_group"
    wrong, rejected = validate_mentions([item.model_copy(update={"kind": "gene"})], [part], policy, {})
    assert not wrong and rejected[0]["failures"] == ["single_gene_contains_group_or_process"]


def test_verification_contract_requires_all_observations_and_fields():
    from pydantic import ValidationError

    schema = verification_contract(2)
    item = {
        "source_fact_index": 0,
        "source_target_change": "NO_EFFECT",
        "checks": {name: {"verdict": "SUPPORTED", "reason": "synthetic"} for name in REVIEW_FIELDS},
    }
    with pytest.raises(ValidationError):
        schema.model_validate({"observation_0": item})
    complete = schema.model_validate({"observation_0": item, "observation_1": item})
    assert [r.observation_index for r in unpack_verification(complete).reviews] == [0, 1]
    item["checks"].pop("direction")
    with pytest.raises(ValidationError):
        schema.model_validate({"observation_0": item, "observation_1": item})


def test_scientific_manual_is_system_instruction_not_source_data(policy):
    prompt = system_prompt(policy, "mentions", "Recognize mentions")
    assert policy.stage_instructions["mentions"] in prompt
    assert "untrusted data" in prompt and "gene_group" in prompt


def test_quantity_contract_only_allows_source_table_cells_and_null_for_prose(policy):
    from pydantic import ValidationError

    part = source("The reported count was 10.")
    value = observation().model_dump()
    value["frame_id"] = "frame:synthetic"
    value["quantities"] = [
        {
            "part_id": "p:1",
            "cell_ref": None,
            "raw_value": "10",
            "units": "count",
            "comparison": None,
            "origin": "author_reported",
        }
    ]
    payload = {"observations": [value], "missing_mentions": [], "overflow": False, "missing_context": []}
    _, prose_schema = contracts(policy, [part])
    prose_schema.model_validate(payload)
    value["quantities"][0]["cell_ref"] = part["text"]
    with pytest.raises(ValidationError):
        prose_schema.model_validate(payload)
    part["cells"] = [{"col_start": 2, "raw_value": "10"}]
    _, table_schema = contracts(policy, [part])
    value["quantities"][0]["cell_ref"] = "p:1:c2"
    table_schema.model_validate(payload)
    value["quantities"][0]["cell_ref"] = "p:1:c99"
    with pytest.raises(ValidationError):
        table_schema.model_validate(payload)


def test_mentions_require_original_spans_and_species_evidence(policy):
    part = source("GeneA increased in the experiment.")
    item = Mention(
        surface="GeneA",
        kind="gene",
        part_id=part["part_id"],
        anchor=part["text"],
        species="Mus musculus",
        species_evidence=None,
    )
    valid, rejected = validate_mentions([item], [part], policy, {})
    assert len(valid) == 1 and not rejected
    assert valid[0]["species"] is None and valid[0]["species_proposed"] == "Mus musculus"
    assert valid[0]["annotation_issues"] == ["species_without_source_evidence"]
    item = item.model_copy(update={"species": None, "surface": "GeneB"})
    assert not validate_mentions([item], [part], policy, {})[0]


def test_species_aliases_and_true_conflicts_are_distinct(policy):
    part = source("GeneA was measured in mouse and human cells.")
    base = Mention(
        surface="GeneA",
        kind="gene",
        part_id=part["part_id"],
        anchor=part["text"],
        species="mouse",
        species_evidence=Citation(part_id=part["part_id"], quote=part["text"]),
    )
    alias = base.model_copy(update={"species": "Mus musculus"})
    valid, rejected = validate_mentions([base, alias], [part], policy, {})
    assert valid[0]["species"] == "Mus musculus" and not rejected
    conflict = base.model_copy(update={"species": "human"})
    valid, rejected = validate_mentions([base, conflict, alias], [part], policy, {})
    assert valid[0]["species"] is None and rejected


def observation(relation="PERTURBATION_EFFECT", direction="NO_EFFECT"):
    return Observation(
        subject_id="a",
        object_id="b",
        relation=relation,
        evidence_classification=dict(
            evidence_type=None,
            directness="FUNCTIONAL",
            experimental_outcome="NO_DETECTED_EFFECT",
            statement_status="NEGATED",
            measured_or_inferred="measured",
            regulatory_direction="UNKNOWN",
        ),
        measured_variable="GeneB expression",
        measurement_evidence=Citation(part_id="p:1", quote="DrugA did not change GeneB expression."),
        observed_change=direction,
        intervention="DrugA",
        comparison="control",
        outcome="negative_or_null",
        statement_status="primary_result",
        directness="not_established",
        context=dict(species=None, tissue=None, cell_type=None, condition=None, model_system=None),
        assay=None,
        experiment_label=None,
        assertion="DrugA did not change GeneB expression.",
        citations=[Citation(part_id="p:1", quote="DrugA did not change GeneB expression.")],
        quantities=[],
        limitations=[],
    )


def test_chemical_null_effect_allowed_but_not_gene_regulation(policy):
    parts = [source("DrugA did not change GeneB expression.")]
    mentions = {"a": {"kind": "chemical"}, "b": {"kind": "gene"}}
    assert observation_failures(observation(), mentions, policy, parts) == []
    assert "relation_endpoint_type_not_allowed" in observation_failures(
        observation("REGULATES"), mentions, policy, parts
    )
    assert observation_failures(observation(), {}, policy, parts) == ["endpoint_not_in_validated_inventory"]


def test_enrichment_never_establishes_process_activity(policy):
    obs = observation("ENRICHMENT_ASSOCIATION", "INCREASE")
    mentions = {"a": {"kind": "gene_group"}, "b": {"kind": "process"}}
    assert "enrichment_is_not_process_activity_change" in observation_failures(
        obs, mentions, policy, [source(obs.assertion)]
    )


def test_independent_read_and_field_coverage_gate_verifier_approval():
    obs = observation()
    read = SourceRead(
        facts=[
            SourceFact(
                subject_surface="DrugA",
                object_surface="GeneB",
                measured_variable="GeneB expression",
                observed_change="INCREASE",
                intervention="DrugA",
                evidence=obs.citations[0],
            )
        ],
        overflow=False,
    )
    checks = [FieldCheck(field=f, verdict="SUPPORTED", reason="synthetic") for f in sorted(REVIEW_FIELDS)]
    review = ObservationReview(
        observation_index=0, source_fact_index=0, source_target_change="NO_EFFECT", checks=checks
    )
    result = review_finding(0, obs, [review], read, [source(obs.assertion)])
    assert result.status == "UNSUPPORTED"
    assert "independent_source_direction_disagrees" in result.field_issues
    review.checks[-1] = review.checks[0]
    assert review_finding(0, obs, [review], read, [source(obs.assertion)]) is None


def test_corpus_stopped_guard_does_not_make_calls(tmp_path, monkeypatch):
    from regkg.workflows.extraction_corpus import main

    p = tmp_path / "data/work/p4-corpus"
    p.mkdir(parents=True)
    (p / "status.json").write_text('{"restart_authorized":false}')
    monkeypatch.chdir(tmp_path)
    with pytest.raises(RuntimeError, match="Full corpus remains stopped"):
        main()


def test_external_gene_identity_requires_species_and_alias_agreement():
    from regkg.extraction.schemas import Entity
    from regkg.extraction.validation import EntityResolver

    catalog = {
        "source": "synthetic",
        "retrieved_utc": "synthetic",
        "response": {
            "result": {
                "123": {
                    "uid": "123",
                    "name": "GeneA",
                    "otheraliases": "AliasA",
                    "organism": {"scientificname": "Mus musculus"},
                }
            }
        },
    }
    resolver = EntityResolver([], "synthetic", catalog)
    hints = [{"external_identifier": "123"}]
    mouse = Entity(name="GeneA", kind="gene", species="Mus musculus")
    assert resolver.resolve(mouse, hints)["ncbi_gene_id"] == "123"
    assert resolver.resolve(mouse.model_copy(update={"species": None}), hints)["entity_id"] is None
    assert resolver.resolve(mouse.model_copy(update={"species": "Homo sapiens"}), hints)["entity_id"] is None
    assert (
        resolver.resolve(mouse.model_copy(update={"name": "GeneB"}), hints)["mapping_status"]
        == "annotation_name_conflict"
    )
