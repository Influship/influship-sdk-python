# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.creator_basic import CreatorBasic
from .shared.profile_summary import ProfileSummary

__all__ = ["CreatorLookalikeResponse", "Data", "DataSimilarity"]


class DataSimilarity(BaseModel):
    """Similarity information for lookalike match"""

    score: float
    """Similarity score (0-1)"""

    shared_traits: List[str]
    """Shared traits with seed creators"""


class Data(BaseModel):
    creator: CreatorBasic
    """Basic creator information"""

    primary_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""

    similarity: DataSimilarity
    """Similarity information for lookalike match"""


class CreatorLookalikeResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more results are available"""

    next_cursor: Optional[str] = None
    """Cursor for the next page"""
