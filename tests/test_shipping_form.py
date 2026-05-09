# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
"""Unit tests for ShippingForm vocabulary enum."""
from __future__ import annotations

import pytest

from cxrp.vocabulary.shipping_form import ShippingForm


def test_all_members_present():
    members = {m.name for m in ShippingForm}
    assert members == {"PR", "PATCH", "BRANCH", "ARTIFACT", "COMMIT"}


def test_member_values():
    assert ShippingForm.PR.value == "pr"
    assert ShippingForm.PATCH.value == "patch"
    assert ShippingForm.BRANCH.value == "branch"
    assert ShippingForm.ARTIFACT.value == "artifact"
    assert ShippingForm.COMMIT.value == "commit"


def test_round_trip_from_string():
    for member in ShippingForm:
        assert ShippingForm(member.value) is member


def test_is_str_subclass():
    for member in ShippingForm:
        assert isinstance(member, str)


def test_invalid_value_raises_value_error():
    with pytest.raises(ValueError):
        ShippingForm("invalid_form")
