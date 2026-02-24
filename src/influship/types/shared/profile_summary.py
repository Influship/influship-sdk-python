# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProfileSummary"]


class ProfileSummary(BaseModel):
    """Abbreviated profile information"""

    id: str
    """Profile unique identifier"""

    engagement_rate: Optional[float] = None
    """Engagement rate as a percentage, null if unknown (e.g. 3.5 means 3.5%)"""

    followers: Optional[int] = None
    """Follower count (null if unknown)"""

    is_verified: bool
    """Whether the account is verified"""

    platform: Literal["instagram"]
    """Social media platform"""

    url: str
    """Profile URL"""

    username: str
    """Profile username"""
