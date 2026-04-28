from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ecp.contracts.common import BaseContract


@dataclass
class ExecutionRequest(BaseContract):
    contract_kind: str = "execution_request"
    task_id: str = ""
    lane_decision_id: str = ""
    scope: str = ""
    input_payload: dict[str, Any] = field(default_factory=dict)
    constraints: list[str] = field(default_factory=list)
