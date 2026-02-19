# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatorRetrieveResponse", "Data", "DataProfile"]


class DataProfile(BaseModel):
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


class Data(BaseModel):
    """Full creator details"""

    id: str
    """Creator unique identifier"""

    ai_summary: Optional[str] = None
    """AI-generated summary of the creator"""

    avatar_url: Optional[str] = None
    """Avatar URL"""

    bio: Optional[str] = None
    """Creator bio"""

    content_themes: List[str]
    """Content themes/topics"""

    name: str
    """Creator display name"""

    profiles: Optional[List[DataProfile]] = None
    """Social profiles (only included when include=profiles)"""


class CreatorRetrieveResponse(BaseModel):
    data: Data
    """Full creator details"""
