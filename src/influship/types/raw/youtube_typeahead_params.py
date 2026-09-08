# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["YoutubeTypeaheadParams"]


class YoutubeTypeaheadParams(TypedDict, total=False):
    q: Required[str]
    """Partial search query"""

    country_code: str

    language_code: str
