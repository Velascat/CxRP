# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
"""ExecutionTargetEnvelope — the named CxRP wire-level execution target.

Groups lane + backend + executor + runtime_binding under one explicit
boundary object. As of schema 0.3, all four fields are typed/validated
on the wire — the closed-system simplification described in
``docs/spec/execution_target.md``.

Provenance does NOT belong here — it is deployment-specific and
OC-owned (see ``BoundExecutionTarget`` on the OC side).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from cxrp.contracts.runtime_binding import RuntimeBinding
from cxrp.vocabulary.executor import BackendName, ExecutorName
from cxrp.vocabulary.lane import LaneType


@dataclass(frozen=True)
class ExecutionTargetEnvelope:
    """The portable, CxRP-shaped execution target.

    Schema 0.3 made backend/executor typed enums (was open strings in
    v0.2). Adding a new backend or executor now requires a CxRP minor
    version bump.
    """

    lane: LaneType
    backend: Optional[BackendName] = None
    executor: Optional[ExecutorName] = None
    runtime_binding: Optional[RuntimeBinding] = None
