"""Configuration contracts: project YAML, model selectors, and .env/process/YAML precedence.

Credentials below are dummy strings; the repository's real .env is never read by these tests.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
from dotenv import dotenv_values

from regkg.config import (
    DEFAULT_OLLAMA_BASE_URL,
    SECRET_ENV_NAMES,
    SUPPORTED_ENV_NAMES,
    ConfigError,
    ModelRole,
    ModelSelectorError,
    SelectionStatus,
    load_environment,
    load_project_config,
    parse_model_selector,
    resolve_model_settings,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DUMMY_KEY = "sk-dummy-not-a-real-key-0000"


@pytest.mark.parametrize(
    ("selector", "role", "provider", "model_name"),
    [
        ("ollama:ExampleModel:v1", ModelRole.EMBEDDING, "ollama", "ExampleModel:v1"),
        ("openrouter:Org/Model:variant", ModelRole.CHAT, "openrouter", "Org/Model:variant"),
        ("litellm:Org/Deployment:revision", ModelRole.CHAT, "litellm", "Org/Deployment:revision"),
        (
            "ollama:pankajrajdeo/biomed-embeddings-16l-fp16:latest",
            ModelRole.EMBEDDING,
            "ollama",
            "pankajrajdeo/biomed-embeddings-16l-fp16:latest",
        ),
        ("OpenRouter:z-ai/glm-5.3-flash", ModelRole.CHAT, "openrouter", "z-ai/glm-5.3-flash"),
        ("sentence-transformers:Org/Model", ModelRole.EMBEDDING, "sentence_transformers", "Org/Model"),
        ("groq:llama-x", ModelRole.CHAT, "groq", "llama-x"),
    ],
)
def test_selector_splits_at_first_colon_and_preserves_suffix(selector, role, provider, model_name):
    spec = parse_model_selector(selector, role)
    assert (spec.provider, spec.model_name) == (provider, model_name)
    assert spec.selector == f"{provider}:{model_name}"


@pytest.mark.parametrize(
    ("selector", "role", "message"),
    [
        ("", ModelRole.CHAT, "empty"),
        ("openrouter", ModelRole.CHAT, "provider:model_name"),
        ("openrouter:", ModelRole.CHAT, "provider:model_name"),
        (":model", ModelRole.CHAT, "provider:model_name"),
        ("anthropic:model", ModelRole.CHAT, "unknown model provider"),
        ("open router:model", ModelRole.CHAT, "whitespace"),
        (" openrouter:model", ModelRole.CHAT, "whitespace"),
        ("openrouter: model", ModelRole.CHAT, "leading/trailing whitespace"),
        ("openrouter:model ", ModelRole.CHAT, "leading/trailing whitespace"),
        ("ollama:model:latest", ModelRole.CHAT, "not usable for chat"),
        ("openrouter:org/model", ModelRole.EMBEDDING, "not usable for embedding"),
        ("openrouter:<organization>/<model>", ModelRole.CHAT, "placeholder"),
    ],
)
def test_invalid_selectors_are_rejected(selector, role, message):
    with pytest.raises(ModelSelectorError, match=message):
        parse_model_selector(selector, role)


def test_env_selection_overrides_yaml_and_verifier_inherits():
    settings = resolve_model_settings(
        {"LLM_MODEL": "openrouter:z-ai/glm-5.3-flash", "OPENROUTER_API_KEY": DUMMY_KEY},
        extraction_yaml={"extractor": {"model": "groq:yaml-model"}},
    )
    assert settings.extractor.spec.selector == "openrouter:z-ai/glm-5.3-flash"
    assert settings.extractor.source == "env:LLM_MODEL"
    assert settings.verifier.spec == settings.extractor.spec
    assert settings.verifier.source == "inherited:env:LLM_MODEL"
    assert settings.credential_presence == {"OPENROUTER_API_KEY": True}


def test_explicit_yaml_verifier_keeps_its_override_and_only_selected_keys_are_required():
    settings = resolve_model_settings(
        {"LLM_MODEL": "openrouter:z-ai/glm-5.3-flash"},
        extraction_yaml={"verifier": {"model": "litellm:team/deploy:v2"}},
    )
    assert settings.verifier.spec.selector == "litellm:team/deploy:v2"
    assert settings.missing_credentials == ["LITELLM_API_KEY", "LITELLM_BASE_URL", "OPENROUTER_API_KEY"]
    assert "GROQ_API_KEY" not in settings.credential_presence


def test_blank_llm_model_falls_back_to_yaml_and_absence_is_unconfigured():
    settings = resolve_model_settings({"LLM_MODEL": ""}, extraction_yaml={"extractor": {"model": "groq:m"}})
    assert settings.extractor.spec.selector == "groq:m"
    unconfigured = resolve_model_settings({})
    assert unconfigured.extractor.status is SelectionStatus.UNCONFIGURED
    assert unconfigured.verifier.status is SelectionStatus.UNCONFIGURED
    assert unconfigured.credential_presence == {}
    placeholder = resolve_model_settings({}, extraction_yaml={"extractor": {"model": "litellm:<proxy-model-alias>"}})
    assert placeholder.extractor.status is SelectionStatus.UNCONFIGURED
    assert placeholder.extractor.reason == "placeholder selector"


def test_process_env_wins_over_dotenv_even_when_empty(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text(
        'LLM_MODEL="openrouter:z-ai/glm-5.3-flash"\n'
        "EMBEDDING_MODEL=ollama:pankajrajdeo/biomed-embeddings-16l-fp16:latest\n"
        f"OPENROUTER_API_KEY={DUMMY_KEY}\n"
        "OLLAMA_BASE_URL=http://localhost:11434\n"
        "INTERPOLATED=${OPENROUTER_API_KEY}\n",
        encoding="utf-8",
    )
    merged = load_environment(env_file, process_env={"LLM_MODEL": "", "EMBEDDINGS_ENABLED": "true"})
    assert merged["LLM_MODEL"] == ""  # explicitly empty process value masks the file
    assert merged["INTERPOLATED"] == "${OPENROUTER_API_KEY}"  # interpolation disabled
    settings = resolve_model_settings(merged, extraction_yaml={"extractor": {"model": "groq:yaml-model"}})
    assert settings.extractor.spec.selector == "groq:yaml-model"
    assert settings.embeddings.status is SelectionStatus.CONFIGURED
    assert settings.embeddings.spec.model_name == "pankajrajdeo/biomed-embeddings-16l-fp16:latest"
    assert settings.ollama_base_url == "http://localhost:11434"
    quoted = load_environment(env_file, process_env={})
    assert parse_model_selector(quoted["LLM_MODEL"], ModelRole.CHAT).model_name == "z-ai/glm-5.3-flash"


@pytest.mark.parametrize("value", ["True", "1", "yes", "", " true"])
def test_embeddings_enabled_is_strictly_boolean(value):
    with pytest.raises(ConfigError, match="exactly 'true' or 'false'"):
        resolve_model_settings({"EMBEDDINGS_ENABLED": value, "EMBEDDING_MODEL": "ollama:m:latest"})


def test_embedding_enablement_precedence_and_defaults():
    yaml_on = {"embeddings": {"enabled": True, "model": "sentence_transformers:Org/Model"}}
    assert resolve_model_settings({}, literature_yaml=yaml_on).embeddings.status is SelectionStatus.CONFIGURED
    off = resolve_model_settings({"EMBEDDINGS_ENABLED": "false"}, literature_yaml=yaml_on)
    assert off.embeddings.status is SelectionStatus.DISABLED
    assert resolve_model_settings({"EMBEDDING_MODEL": "ollama:m:latest"}).embeddings.status is SelectionStatus.DISABLED
    with pytest.raises(ConfigError, match="no real embedding selector"):
        resolve_model_settings({"EMBEDDINGS_ENABLED": "true"})
    with pytest.raises(ModelSelectorError, match="not usable for embedding"):
        resolve_model_settings({"EMBEDDINGS_ENABLED": "false", "EMBEDDING_MODEL": "groq:m"})


def test_ollama_url_default_override_and_credential_rejection():
    enabled = {"EMBEDDINGS_ENABLED": "true", "EMBEDDING_MODEL": "ollama:m:latest"}
    assert resolve_model_settings({**enabled, "OLLAMA_BASE_URL": ""}).ollama_base_url == DEFAULT_OLLAMA_BASE_URL
    assert resolve_model_settings(enabled).ollama_base_url == DEFAULT_OLLAMA_BASE_URL
    override = resolve_model_settings({**enabled, "OLLAMA_BASE_URL": "http://10.0.0.5:11434"})
    assert override.ollama_base_url == "http://10.0.0.5:11434"
    with pytest.raises(ConfigError, match="must not embed credentials"):
        resolve_model_settings({**enabled, "OLLAMA_BASE_URL": "http://user:pw@localhost:11434"})


def test_missing_key_is_reported_by_name_and_values_never_appear_in_records():
    settings = resolve_model_settings({"LLM_MODEL": "openrouter:z-ai/glm-5.3-flash", "OPENROUTER_API_KEY": ""})
    assert settings.missing_credentials == ["OPENROUTER_API_KEY"]
    present = resolve_model_settings({"LLM_MODEL": "openrouter:z-ai/glm-5.3-flash", "OPENROUTER_API_KEY": DUMMY_KEY})
    assert DUMMY_KEY not in repr(present) and DUMMY_KEY not in str(present.to_record())


def test_verify_config_command_prints_presence_not_values(tmp_path):
    (tmp_path / ".env").write_text(f"LLM_MODEL=openrouter:z-ai/glm-5.3-flash\nOPENROUTER_API_KEY={DUMMY_KEY}\n")
    result = subprocess.run(
        [sys.executable, "-m", "regkg", "verify", "config", "--repo-root", str(tmp_path)],
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin"},
        check=True,
    )
    assert '"OPENROUTER_API_KEY": true' in result.stdout
    assert DUMMY_KEY not in result.stdout + result.stderr


def test_model_config_imports_no_model_sdk():
    code = (
        "import sys, regkg.cli, regkg.config\n"
        "banned = [m for m in sys.modules if m.split('.')[0] in "
        "{'langchain', 'langchain_core', 'langchain_openrouter', 'langchain_litellm', 'langchain_groq', "
        "'langchain_ollama', 'langchain_huggingface', 'sentence_transformers', 'torch', 'neo4j', 'httpx'}]\n"
        "print(banned)\n"
    )
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "[]"


def test_env_example_contract():
    values = dotenv_values(REPO_ROOT / ".env.example", interpolate=False)
    assert set(values) <= SUPPORTED_ENV_NAMES
    assert all(not values[name] for name in SECRET_ENV_NAMES & set(values))  # credentials stay blank
    settings = resolve_model_settings({k: v for k, v in values.items() if v is not None})
    assert settings.extractor.spec.selector == "openrouter:z-ai/glm-5.3-flash"
    assert settings.embeddings.spec.model_name == "pankajrajdeo/biomed-embeddings-16l-fp16:latest"
    assert settings.missing_credentials == ["OPENROUTER_API_KEY"]


def test_project_config_rejects_unknown_fields(synthetic_project):
    loaded = load_project_config(synthetic_project, repo_root=synthetic_project.parents[1])
    assert loaded.resolve(loaded.config.chromlinker.path) == synthetic_project.parents[1] / "files" / "chromlinker.csv"
    text = synthetic_project.read_text()
    synthetic_project.write_text(text.replace("tissue: lung", "tissue: lung\n  tisue: lung"))
    with pytest.raises(ConfigError, match="tisue"):
        load_project_config(synthetic_project, repo_root=synthetic_project.parents[1])


def test_real_project_config_is_valid_and_covers_scope():
    loaded = load_project_config(REPO_ROOT / "configs" / "project.yaml")
    config = loaded.config
    assert loaded.repo_root == REPO_ROOT
    assert config.input_mode.value == "real"
    assert config.at1_scope.tf_seeds == ["TEAD1", "KLF5", "GATA6", "FOXA2", "ETV1"]
    assert {d.focal_cell_type for d in config.niche_definitions} <= set(config.cell_types)
    assert config.dataset.conditions["Control"].disease is None
