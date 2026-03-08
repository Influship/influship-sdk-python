# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["MatchInfo"]


class MatchInfo(BaseModel):
    """Search match information"""

    reasons: List[str]
    """Human-readable match reasons"""

    score: float
    """Match relevance score (0-1)"""
