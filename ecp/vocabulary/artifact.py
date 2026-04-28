from enum import Enum


class ArtifactType(str, Enum):
    """Canonical artifact vocabulary for ExecutionResult payloads."""

    INPUT = "input"
    OUTPUT = "output"
    LOG = "log"
    DIAGNOSTIC = "diagnostic"
