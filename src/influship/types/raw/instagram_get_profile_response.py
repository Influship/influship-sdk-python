# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InstagramGetProfileResponse", "Data", "DataActivity", "DataGrowth", "DataMetrics", "DataPost"]


class DataActivity(BaseModel):
    last_post_at: Optional[datetime] = None
    """Timestamp of last post"""


class DataGrowth(BaseModel):
    followers_30d_pct: float
    """Follower growth percentage over 30 days (e.g. 2.5 means +2.5%)"""


class DataMetrics(BaseModel):
    avg_comments_recent: float
    """Average comments on recent posts"""

    avg_likes_recent: float
    """Average likes on recent posts"""

    avg_views_recent: Optional[float] = None
    """Average views on recent posts"""

    engagement_rate: float
    """Engagement rate as a percentage (e.g. 3.5 means 3.5%)"""

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


class DataPost(BaseModel):
    """Simplified post from live scrape"""

    id: str
    """Post unique identifier"""

    caption: Optional[str] = None
    """Post caption"""

    comments_count: Optional[int] = None
    """Comment count"""

    likes_count: Optional[int] = None
    """Like count"""

    media_url: Optional[str] = None
    """Primary media URL"""

    platform_id: str
    """Platform-specific post ID"""

    posted_at: datetime
    """Post timestamp"""

    type: Literal["image", "video", "carousel", "reel", "story"]
    """Type of post"""

    url: str
    """Post URL"""


class Data(BaseModel):
    """Live scraped profile data"""

    id: str
    """Profile unique identifier"""

    activity: DataActivity

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
    """External website URL"""

    growth: DataGrowth

    is_business: bool
    """Whether this is a business account"""

    is_private: bool
    """Whether the account is private"""

    is_verified: bool
    """Whether the account is verified"""

    metrics: DataMetrics

    platform: Literal["instagram"]
    """Social media platform"""

    pronouns: Optional[List[str]] = None
    """Listed pronouns"""

    scraped_at: datetime
    """When this data was scraped"""

    url: str
    """Profile URL"""

    username: str
    """Profile username"""

    posts: Optional[List[DataPost]] = None
    """Recent posts (only included when include_posts=true)"""


class InstagramGetProfileResponse(BaseModel):
    data: Data
    """Live scraped profile data"""
