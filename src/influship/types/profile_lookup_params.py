# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProfileLookupParams", "Profile"]


class ProfileLookupParams(TypedDict, total=False):
    profiles: Required[Iterable[Profile]]
    """Profiles to lookup"""


class Profile(TypedDict, total=False):
    platform: Required[Literal["instagram"]]
    """Social media platform"""

    username: Required[str]
    """Username to lookup"""
