"""Retriever placeholder module.

The production pipeline currently builds Chroma retrievers inside pipeline.py.
This module provides a stable import location for future refactoring.
"""

from typing import List


def retrieve(query: str, top_k: int = 8) -> List[str]:
    _ = query
    _ = top_k
    return []

