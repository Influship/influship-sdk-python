# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TiktokListProfileVideosParams"]


class TiktokListProfileVideosParams(TypedDict, total=False):
    cursor: str
    """Opaque cursor from the previous response"""

    region: str
    """Two-letter region code"""

    sort_by: Literal["latest", "popular"]
    """Video ordering"""
