from enum import Enum


class ExecutionStatus(str, Enum):
    """Canonical execution status vocabulary for ECP contracts."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
