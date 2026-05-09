# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
from enum import Enum


class ShippingForm(str, Enum):
    """Canonical shipping-form vocabulary for CxRP contracts.

    Describes how a code contribution is delivered from an agent to its
    integration target (e.g. a PR, a raw patch file, a branch push, a
    pre-built artifact, or an individual commit reference).
    """

    PR = "pr"
    PATCH = "patch"
    BRANCH = "branch"
    ARTIFACT = "artifact"
    COMMIT = "commit"
