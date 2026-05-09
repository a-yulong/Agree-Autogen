from pathlib import Path


def test_requirement_prompt_requires_grounded_identifiers():
    prompt = Path("prompts/requirement_analyst_prompt.txt").read_text(encoding="utf-8")
    assert "Do not introduce identifiers" in prompt
    assert "unresolved_terms" in prompt
    assert "assumptions" in prompt
    assert "guarantees" in prompt

