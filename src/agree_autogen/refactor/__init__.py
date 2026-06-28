"""Refactored AGREE-AutoGen implementation.

This package contains the new experiment-oriented pipeline used by the local
runner.  The legacy modules are kept only as historical code until the new
pipeline is fully validated across the benchmark.
"""

from .orchestrator import RefactoredAgreeAutogenPipeline

__all__ = ["RefactoredAgreeAutogenPipeline"]
