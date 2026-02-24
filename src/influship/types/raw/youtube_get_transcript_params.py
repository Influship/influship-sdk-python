# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["YoutubeGetTranscriptParams"]


class YoutubeGetTranscriptParams(TypedDict, total=False):
    language: str
    """Language code or "auto" for automatic detection"""
