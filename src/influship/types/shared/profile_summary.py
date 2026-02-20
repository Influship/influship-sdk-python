# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProfileSummary"]


class ProfileSummary(BaseModel):
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
