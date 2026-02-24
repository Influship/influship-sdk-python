# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PostListResponse", "Location", "Media", "Metrics"]


class Location(BaseModel):
    """Post location information"""

    name: Optional[str] = None
    """Location name"""


class Media(BaseModel):
    """Post media information"""

    duration_seconds: Optional[float] = None
    """Video duration in seconds"""

    thumbnail_url: Optional[str] = None
    """Thumbnail URL"""

    url: Optional[str] = None
    """Media URL"""

    video_url: Optional[str] = None
    """Video URL (for video content)"""


class Metrics(BaseModel):
    """Post engagement metrics"""

    comments: Optional[int] = None
    """Comment count"""

    engagement_rate: Optional[float] = None
    """Engagement rate for this post as a percentage (e.g. 3.8 means 3.8%)"""

    likes: Optional[int] = None
    """Like count"""

    shares: Optional[int] = None
    """Share count"""

    views: Optional[int] = None
    """View count (for video content)"""


class PostListResponse(BaseModel):
    """Full post details"""

    id: str
    """Post unique identifier"""

    caption: Optional[str] = None
    """Post caption"""

    hashtags: List[str]
    """Hashtags used in the post"""

    location: Optional[Location] = None
    """Post location information"""

    media: Media
    """Post media information"""

    mentions: List[str]
    """Usernames mentioned in the post"""

    metrics: Metrics
    """Post engagement metrics"""

    platform: Literal["instagram"]
    """Social media platform"""

    platform_id: str
    """Platform-specific post ID"""

    posted_at: datetime
    """Post timestamp"""

    profile_id: str
    """Profile unique identifier"""

    type: Literal["image", "video", "carousel", "reel", "story"]
    """Type of post"""

    url: str
    """Post URL"""
