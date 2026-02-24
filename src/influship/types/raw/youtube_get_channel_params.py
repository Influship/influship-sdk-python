# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["YoutubeGetChannelParams"]


class YoutubeGetChannelParams(TypedDict, total=False):
    include_videos: bool
    """Include recent videos in response"""

    video_limit: int
    """Number of videos to include"""
