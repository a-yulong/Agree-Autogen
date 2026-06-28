from pathlib import Path


def test_requirement_prompt_requires_grounded_identifiers():
    prompt = Path("prompts/requirement_analyst.txt").read_text(encoding="utf-8")
    assert "Do not create new AADL identifiers" in prompt
    assert "unresolved_semantics" in prompt
    assert "candidate_polarity" in prompt
    assert "anchored_identifiers" in prompt

