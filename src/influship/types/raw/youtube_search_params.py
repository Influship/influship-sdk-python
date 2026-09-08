# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["YoutubeSearchParams"]


class YoutubeSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    content_type: Literal["all", "videos"]
    """Return all result types or only videos"""

    country_code: str
    """Country code for localized results (ISO 3166-1 alpha-2)"""

    cursor: str
    """Opaque cursor from next_cursor to fetch the next result page"""

    duration: Literal["any", "short", "medium", "long"]
    """Filter videos by YouTube duration band"""

    language_code: str
    """Language code for results"""

    limit: int
    """Maximum number of results to return"""

    sort_by: Literal["relevance", "popular"]
    """Order results by relevance or view popularity"""

    upload_date: Literal["any", "last_hour", "today", "this_week", "this_month", "this_year"]
    """Only return results uploaded within the selected window"""
