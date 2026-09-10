# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TiktokGetMusicParams"]


class TiktokGetMusicParams(TypedDict, total=False):
    music_id: Required[str]
    """TikTok sound clip ID, not a recording or album ID"""
