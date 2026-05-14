# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstagramGetTranscriptParams"]


class InstagramGetTranscriptParams(TypedDict, total=False):
    language: str
    """Optional language code for transcription. Omit to auto-detect."""
