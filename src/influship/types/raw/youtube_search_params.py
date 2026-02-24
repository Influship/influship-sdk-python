# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["YoutubeSearchParams"]


class YoutubeSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    country_code: str
    """Country code for localized results (ISO 3166-1 alpha-2)"""

    language_code: str
    """Language code for results"""

    limit: int
    """Maximum number of results to return"""
