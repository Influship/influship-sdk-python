# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PostListParams"]


class PostListParams(TypedDict, total=False):
    creator_id: str
    """Creator ID (use this OR platform+username)"""

    cursor: str
    """Pagination cursor for next page"""

    limit: int
    """Maximum posts to return"""

    platform: Literal["instagram"]
    """Platform (required with username)"""

    sort: Literal["recent", "top_engagement", "most_likes", "most_views", "most_comments"]
    """Sort order"""

    username: str
    """Username (required with platform)"""
