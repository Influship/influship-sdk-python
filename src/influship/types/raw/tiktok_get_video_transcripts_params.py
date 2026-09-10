# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TiktokGetVideoTranscriptsParams"]


class TiktokGetVideoTranscriptsParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]

    mode: Literal["auto", "captions"]
