# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CreatorAutocompleteParams"]


class CreatorAutocompleteParams(TypedDict, total=False):
    q: Required[str]
    """Search query (min 2 characters)"""

    limit: str
    """Maximum results to return"""

    platform: Literal["instagram"]
    """Filter by platform"""

    scope: Literal["creator_only", "matched_platforms", "all_platforms"]
    """Which platforms to include in results"""
