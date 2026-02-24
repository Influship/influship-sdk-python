# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstagramGetProfileParams"]


class InstagramGetProfileParams(TypedDict, total=False):
    include_posts: bool
    """Include recent posts in response"""

    post_limit: int
    """Number of posts to include"""
