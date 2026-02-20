# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.profile_summary import ProfileSummary

__all__ = ["CreatorLookalikeResponse", "Data", "DataCreator", "DataSimilarity"]


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


class DataSimilarity(BaseModel):
    """Similarity information for lookalike match"""

    score: float
    """Similarity score (0-1)"""

    shared_traits: List[str]
    """Shared traits with seed creators"""


class Data(BaseModel):
    creator: DataCreator
    """Basic creator information"""

    primary_profile: ProfileSummary
    """Abbreviated profile information"""

    similarity: DataSimilarity
    """Similarity information for lookalike match"""


class CreatorLookalikeResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more results are available"""

    next_cursor: Optional[str] = None
    """Cursor for the next page"""

    total: Optional[int] = None
    """Total number of results"""
