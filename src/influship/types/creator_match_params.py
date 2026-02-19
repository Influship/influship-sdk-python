# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CreatorMatchParams", "Creator", "Intent"]


class CreatorMatchParams(TypedDict, total=False):
    creators: Required[Iterable[Creator]]
    """Creators to evaluate"""

    intent: Required[Intent]
    """Campaign intent for creator matching"""


class Creator(TypedDict, total=False):
    """Creator identifier for match endpoint"""

    creator_id: str
    """Creator ID (use this OR platform+username)"""

    platform: Literal["instagram"]
    """Platform (required with username)"""

    username: str
    """Username (required with platform)"""


class Intent(TypedDict, total=False):
    """Campaign intent for creator matching"""

    query: Required[str]
    """Campaign description"""

    context: str
    """Additional context about the campaign"""
