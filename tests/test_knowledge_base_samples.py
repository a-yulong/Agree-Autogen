from pathlib import Path

import yaml


KB_ROOT = Path("knowledge_base")


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def test_knowledge_base_manifest_and_files_parse():
    manifest = load_yaml(KB_ROOT / "curated" / "examples" / "manifest.yaml")
    assert manifest["name"] == "agree-autogen-format-examples"
    for category in manifest["categories"].values():
        for relative in category["files"]:
            path = KB_ROOT / "curated" / "examples" / relative
            assert path.exists(), path
            assert load_yaml(path)


def test_source_inventory_files_parse():
    sources = load_yaml(KB_ROOT / "sources.yaml")
    public_sources = load_yaml(KB_ROOT / "manifests" / "public_sources.yaml")
    local_example = load_yaml(KB_ROOT / "manifests" / "local_sources.example.yaml")
    assert sources["sources"]
    assert public_sources["sources"]
    assert local_example["local_rag_corpus"]["docs_directory"]


def test_knowledge_base_entries_have_id_and_description():
    for path in KB_ROOT.rglob("*.yaml"):
        data = load_yaml(path)
        entries = data.get("rules") or data.get("patterns")
        if entries:
            for entry in entries:
                assert entry.get("id"), path
                assert entry.get("description"), path
                assert entry.get("notes"), path
        if "triplet" in data:
            triplet = data["triplet"]
            assert triplet.get("id"), path
            assert triplet.get("requirement_nl"), path
            assert triplet.get("logic_prop"), path
            assert triplet.get("code_agree"), path
            assert triplet.get("notes"), path
