# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TiktokListCommentRepliesParams"]


class TiktokListCommentRepliesParams(TypedDict, total=False):
    comment_id: Required[str]
    """Numeric ID of the parent comment"""

    url: Required[str]
    """HTTPS TikTok video or share URL"""

    cursor: str
    """Opaque cursor from the previous response"""
