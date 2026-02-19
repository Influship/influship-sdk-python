# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SearchQueryResponse",
    "Data",
    "DataCreator",
    "DataMatch",
    "DataPrimaryProfile",
    "DataRelevantProfile",
    "Pagination",
]


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


class DataPrimaryProfile(BaseModel):
    """Primary profile (largest audience)"""

    id: str
    """Profile unique identifier"""

    engagement_rate: float
    """Engagement rate as percentage"""

    followers: int
    """Follower count"""

    is_verified: bool
    """Whether the account is verified"""

    platform: Literal["instagram"]
    """Social media platform"""

    url: str
    """Profile URL"""

    username: str
    """Profile username"""


class DataRelevantProfile(BaseModel):
    """Most relevant profile based on search query"""

    id: str
    """Profile unique identifier"""

    engagement_rate: float
    """Engagement rate as percentage"""

    followers: int
    """Follower count"""

    is_verified: bool
    """Whether the account is verified"""

    platform: Literal["instagram"]
    """Social media platform"""

    url: str
    """Profile URL"""

    username: str
    """Profile username"""


class Data(BaseModel):
    creator: DataCreator
    """Basic creator information"""

    match: DataMatch
    """Search match information"""

    primary_profile: DataPrimaryProfile
    """Primary profile (largest audience)"""

    relevant_profile: DataRelevantProfile
    """Most relevant profile based on search query"""


class Pagination(BaseModel):
    has_more: bool
    """Whether more results are available"""

    next_cursor: Optional[str] = None
    """Cursor for the next page"""

    total: Optional[int] = None
    """Total number of results"""


class SearchQueryResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
