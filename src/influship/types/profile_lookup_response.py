# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ProfileLookupResponse",
    "Data",
    "DataFound",
    "DataFoundActivity",
    "DataFoundGrowth",
    "DataFoundMetrics",
    "DataNotFound",
]


class DataFoundActivity(BaseModel):
    """Profile activity information"""

    last_post_at: Optional[datetime] = None
    """Timestamp of last post"""


class DataFoundGrowth(BaseModel):
    """Profile growth statistics"""

    followers_30d_pct: float
    """Follower growth percentage over 30 days"""

    monthly_rate: float
    """Monthly growth rate"""


class DataFoundMetrics(BaseModel):
    """Profile performance metrics"""

    avg_comments_recent: float
    """Average comments on recent posts"""

    avg_likes_recent: float
    """Average likes on recent posts"""

    avg_views_recent: Optional[float] = None
    """Average views on recent posts (for video content)"""

    engagement_rate: float
    """Engagement rate as percentage"""

    followers: int
    """Follower count"""

    following: int
    """Following count"""

    posts: int
    """Total post count"""

    posts_last_30d: int
    """Posts in the last 30 days"""

    posts_per_week: float
    """Average posts per week"""


class DataFound(BaseModel):
    """Full profile details"""

    id: str
    """Profile unique identifier"""

    activity: DataFoundActivity
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

    growth: DataFoundGrowth
    """Profile growth statistics"""

    is_business: bool
    """Whether this is a business account"""

    is_private: bool
    """Whether the account is private"""

    is_verified: bool
    """Whether the account is verified"""

    metrics: DataFoundMetrics
    """Profile performance metrics"""

    platform: Literal["instagram"]
    """Social media platform"""

    pronouns: Optional[List[str]] = None
    """Listed pronouns"""

    url: str
    """Profile URL"""

    username: str
    """Profile username"""


class DataNotFound(BaseModel):
    platform: Literal["instagram"]
    """Social media platform"""

    username: str


class Data(BaseModel):
    found: List[DataFound]
    """Profiles that were found"""

    not_found: List[DataNotFound]
    """Profiles that were not found"""


class ProfileLookupResponse(BaseModel):
    data: Data
