# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandSafetyAnalyzeCreatorsParams", "Creator"]


class BrandSafetyAnalyzeCreatorsParams(TypedDict, total=False):
    creators: Required[Iterable[Creator]]
    """Creators to analyze"""


class Creator(TypedDict, total=False):
    creator_id: str
    """Creator ID (use this OR platform+username)"""

    platform: Literal["instagram"]
    """Platform (required with username)"""

    username: str
    """Username (required with platform)"""
