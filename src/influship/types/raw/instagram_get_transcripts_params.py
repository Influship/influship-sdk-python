# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["InstagramGetTranscriptsParams"]


class InstagramGetTranscriptsParams(TypedDict, total=False):
    shortcodes: Required[SequenceNotStr[str]]
    """Instagram video post shortcodes from /p/, /reel/, or /tv/ URLs"""

    language: str
    """Optional language code for transcription. Omit to auto-detect."""
