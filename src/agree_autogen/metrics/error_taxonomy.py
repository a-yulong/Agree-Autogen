"""Rule-based T1-T5 error taxonomy helpers."""

from typing import List


def classify_error(error_text: str) -> List[str]:
    text = (error_text or "").lower()
    labels: List[str] = []
    if any(key in text for key in ["syntax", "missing eof", "mismatched", "extraneous", "token", "parse"]):
        labels.append("T1")
    if any(key in text for key in ["couldn't resolve", "not found", "with clause", "reference", "package", "property set"]):
        labels.append("T2")
    if any(key in text for key in ["subcomponent", "connection", "feature", "implementation", "classifier"]):
        labels.append("T3")
    if any(key in text for key in ["duplicate", "already defined", "identifier", "declaration", "name"]):
        labels.append("T4")
    if any(key in text for key in ["type", "int", "real", "bool", "numeric", "left and right"]):
        labels.append("T5")
    return labels or ["T1"]

