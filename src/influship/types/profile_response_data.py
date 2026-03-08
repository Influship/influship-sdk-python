# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .profile_growth import ProfileGrowth
from .profile_metrics import ProfileMetrics
from .profile_activity import ProfileActivity

__all__ = ["ProfileResponseData"]


class ProfileResponseData(BaseModel):
    """Full profile details"""

    id: str
    """Profile unique identifier"""

    activity: ProfileActivity
    """Profile activity information"""

    avatar_url: Optional[str] = None
    """Avatar URL"""

    bio: Optional[str] = None
    """Profile bio"""

    category: Optional[str] = None
    """Account category"""

    creator_id: str
    """Creator unique identifier"""

    data_updated_at: Optional[datetime] = None
    """Last data refresh timestamp"""

    display_name: Optional[str] = None
    """Display name"""

    external_url: Optional[str] = None
    """External website URL from bio"""

    growth: ProfileGrowth
    """Profile growth statistics"""

    is_business: bool
    """Whether this is a business account"""

    is_private: bool
    """Whether the account is private"""

    is_verified: bool
    """Whether the account is verified"""

    metrics: ProfileMetrics
    """Profile performance metrics"""

    platform: Literal["instagram"]
    """Social media platform"""

    pronouns: Optional[List[str]] = None
    """Listed pronouns"""

    url: str
    """Profile URL"""

    username: str
    """Profile username"""
