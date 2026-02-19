# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandSafetyAnalyzePostsParams", "Post"]


class BrandSafetyAnalyzePostsParams(TypedDict, total=False):
    posts: Required[Iterable[Post]]
    """Posts to analyze"""


class Post(TypedDict, total=False):
    platform: Literal["instagram"]
    """Platform (required with platform_id)"""

    platform_id: str
    """Platform-specific post ID"""

    post_id: str
    """Internal post ID"""

    url: str
    """Post URL"""
