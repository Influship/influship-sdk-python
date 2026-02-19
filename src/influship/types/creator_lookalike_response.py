# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatorLookalikeResponse", "Data", "DataCreator", "DataPrimaryProfile", "DataSimilarity", "Pagination"]


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


class DataPrimaryProfile(BaseModel):
    """Abbreviated profile information"""

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


class DataSimilarity(BaseModel):
    """Similarity information for lookalike match"""

    score: float
    """Similarity score (0-1)"""

    shared_traits: List[str]
    """Shared traits with seed creators"""


class Data(BaseModel):
    creator: DataCreator
    """Basic creator information"""

    primary_profile: DataPrimaryProfile
    """Abbreviated profile information"""

    similarity: DataSimilarity
    """Similarity information for lookalike match"""


class Pagination(BaseModel):
    has_more: bool
    """Whether more results are available"""

    next_cursor: Optional[str] = None
    """Cursor for the next page"""

    total: Optional[int] = None
    """Total number of results"""


class CreatorLookalikeResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
