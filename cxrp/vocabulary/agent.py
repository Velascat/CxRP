# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
from enum import Enum


class AgentTopology(str, Enum):
    """Canonical agent topology vocabulary for CxRP contracts."""

    SINGLE = "single"
    PAIR = "pair"
    SWARM = "swarm"
    HIERARCHICAL = "hierarchical"
    PIPELINE = "pipeline"
