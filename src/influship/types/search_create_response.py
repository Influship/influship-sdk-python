# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.profile_summary import ProfileSummary

__all__ = ["SearchCreateResponse", "Data", "DataCreator", "DataMatch"]


class DataCreator(BaseModel):
    """Basic creator information"""

    id: str
    """Creator unique identifier"""

    avatar_url: Optional[str] = None
    """Avatar URL"""

    bio: Optional[str] = None
    """Creator bio"""

    name: str
    """Creator display name"""


class DataMatch(BaseModel):
    """Search match information"""

    reasons: List[str]
    """Human-readable match reasons"""

    score: float
    """Match relevance score (0-1)"""


class Data(BaseModel):
    creator: DataCreator
    """Basic creator information"""

    match: DataMatch
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
