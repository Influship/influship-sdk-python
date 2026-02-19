# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CreatorLookalikeParams", "Seed", "Filters", "FiltersEngagementRate", "FiltersFollowers"]


class CreatorLookalikeParams(TypedDict, total=False):
    seeds: Required[Iterable[Seed]]
    """Seed creators to find similar creators for"""

    cursor: str
    """Pagination cursor for next page"""

    filters: Filters
    """Additional filters"""

    limit: int
    """Maximum results to return"""


class Seed(TypedDict, total=False):
    """Seed creator for lookalike search"""

    creator_id: str
    """Creator ID (use this OR platform+username)"""

    platform: Literal["instagram"]
    """Platform (required with username)"""

    username: str
    """Username (required with platform)"""

    weight: float
    """Weight for this seed (0-1)"""


class FiltersEngagementRate(TypedDict, total=False):
    """Filter by engagement rate"""

    max: float
    """Maximum engagement rate (%)"""

    min: float
    """Minimum engagement rate (%)"""


class FiltersFollowers(TypedDict, total=False):
    """Filter by follower count"""

    max: float
    """Maximum follower count"""

    min: float
    """Minimum follower count"""


class Filters(TypedDict, total=False):
    """Additional filters"""

    engagement_rate: FiltersEngagementRate
    """Filter by engagement rate"""

    followers: FiltersFollowers
    """Filter by follower count"""

    verified: bool
    """Filter by verified status"""
