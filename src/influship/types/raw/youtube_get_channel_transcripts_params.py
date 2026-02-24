# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["YoutubeGetChannelTranscriptsParams"]


class YoutubeGetChannelTranscriptsParams(TypedDict, total=False):
    include_segments: bool
    """Include timestamped transcript segments in response"""

    language: str
    """Language code for transcripts"""

    sort_by: Literal["popular", "newest", "oldest"]
    """How to sort channel videos before selecting"""

    video_limit: int
    """Number of videos to fetch transcripts for (max 20)"""
