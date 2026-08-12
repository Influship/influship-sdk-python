# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TiktokListVideoCommentsParams"]


class TiktokListVideoCommentsParams(TypedDict, total=False):
    url: Required[str]
    """HTTPS TikTok video or share URL"""

    cursor: str
    """Opaque cursor from the previous response"""
