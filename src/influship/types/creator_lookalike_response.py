# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.creator_basic import CreatorBasic
from .shared.profile_summary import ProfileSummary

__all__ = ["CreatorLookalikeResponse", "Similarity"]


class Similarity(BaseModel):
    """Similarity information for lookalike match"""

    score: float
    """Similarity score (0-1)"""

    shared_traits: List[str]
    """Shared traits with seed creators"""


class CreatorLookalikeResponse(BaseModel):
    creator: CreatorBasic
    """Basic creator information"""

    primary_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""

    similarity: Similarity
    """Similarity information for lookalike match"""
