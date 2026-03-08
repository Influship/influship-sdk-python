# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .match_info import MatchInfo
from .shared.creator_basic import CreatorBasic
from .shared.profile_summary import ProfileSummary

__all__ = ["SearchCreateResponse", "Data"]


class Data(BaseModel):
    creator: CreatorBasic
    """Basic creator information"""

    match: MatchInfo
    """Search match information"""

    primary_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""

    relevant_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""


class SearchCreateResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more results are available"""

    next_cursor: Optional[str] = None
    """Cursor for the next page"""

    search_id: str
    """Search ID. Use with GET /v1/search/{id} for free pagination."""

    total: int
    """Total number of results across all pages"""
