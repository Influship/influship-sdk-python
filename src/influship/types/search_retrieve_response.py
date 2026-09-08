# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .match_info import MatchInfo
from .shared.creator_basic import CreatorBasic
from .shared.profile_summary import ProfileSummary

__all__ = ["SearchRetrieveResponse"]


class SearchRetrieveResponse(BaseModel):
    creator: CreatorBasic
    """Basic creator information"""

    location_unverified: Optional[bool] = None
    """
    True when the query required a country but this creator location is unverified;
    false when the known location satisfies it; null when the query set no geography
    requirement. Known mismatches are excluded from results.
    """

    match: MatchInfo
    """Search match information"""

    primary_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""

    relevant_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""
