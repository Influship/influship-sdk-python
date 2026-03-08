# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.creator_basic import CreatorBasic
from .shared.profile_summary import ProfileSummary

__all__ = ["SearchRetrieveResponse", "Match"]


class Match(BaseModel):
    """Search match information"""

    reasons: List[str]
    """Human-readable match reasons"""

    score: float
    """Match relevance score (0-1)"""


class SearchRetrieveResponse(BaseModel):
    creator: CreatorBasic
    """Basic creator information"""

    match: Match
    """Search match information"""

    primary_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""

    relevant_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""
