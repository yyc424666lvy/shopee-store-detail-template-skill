from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={f"3pf{i:02d}" for i in range(1,12)}|{f"sp{i:02d}" for i in range(1,18)}

def test_skill_frontmatter():
    text=(ROOT/"SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\n")
    assert "name: shopee-store-detail-template" in text

def test_exactly_28_store_files():
    actual={p.stem for p in (ROOT/"references"/"stores").glob("*.md")}
    assert actual==EXPECTED

def test_store_heading_matches_filename():
    for p in (ROOT/"references"/"stores").glob("*.md"):
        text=p.read_text(encoding="utf-8")
        assert re.search(rf"^###\s+{re.escape(p.stem)}\b", text, re.M)

def test_no_duplicate_sp03_file():
    assert len(list((ROOT/"references"/"stores").glob("sp03.md")))==1

def test_required_release_files_exist():
    required={"SKILL.md", "README.md", "VERSION", "CHANGELOG.md", "LICENSE", "install.ps1", "uninstall.ps1"}
    assert required <= {p.name for p in ROOT.iterdir()}
    assert (ROOT/"scripts"/"doctor.py").is_file()
    assert (ROOT/"references"/"store-index.md").is_file()

def test_store_index_has_exactly_the_supported_ids():
    index=(ROOT/"references"/"store-index.md").read_text(encoding="utf-8")
    indexed=set(re.findall(r"references/stores/([a-z0-9]+)\.md", index))
    assert indexed==EXPECTED

def test_routing_contract_rejects_unknown_and_isolates_batch_outputs():
    skill=(ROOT/"SKILL.md").read_text(encoding="utf-8")
    assert "Never invent a store ID" in skill
    assert "do not guess malformed IDs" in skill
    assert "process each store independently from the same source product detail" in skill
    assert "Never use one generated store output as the source for the next store" in skill

def test_product_fact_preservation_contract():
    skill=(ROOT/"SKILL.md").read_text(encoding="utf-8")
    assert "Never change product facts, claims, quantities, materials, sizes, package contents" in skill
    assert "product facts remain unchanged" in skill

def test_special_template_fidelity_markers():
    for sid in ("sp06", "sp10", "sp11"):
        text=(ROOT/"references"/"stores"/f"{sid}.md").read_text(encoding="utf-8")
        assert "【Label：Value" in text
    sp14=(ROOT/"references"/"stores"/"sp14.md").read_text(encoding="utf-8")
    assert "（不写 Features）" in sp14
