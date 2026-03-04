# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchCreateParams", "Filters", "FiltersEngagementRate", "FiltersFollowers"]


class SearchCreateParams(TypedDict, total=False):
    query: Required[str]
    """Natural language search query"""

    filters: Filters
    """Additional filters"""

    limit: int
    """Maximum results to return"""

    platforms: List[Literal["instagram"]]
    """Filter results to specific platforms"""


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
