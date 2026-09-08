# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PostListResponse", "Location", "Media", "MediaCarouselItem", "Metrics"]


class Location(BaseModel):
    """Post location information"""

    name: Optional[str] = None
    """Location name"""


class MediaCarouselItem(BaseModel):
    index: int
    """Zero-based position in the carousel."""

    is_video: bool
    """True if this item is a video."""

    thumbnail_url: Optional[str] = None
    """Thumbnail URL for this item. Cover frame for videos."""


class Media(BaseModel):
    """Post media information"""

    carousel_items: Optional[List[MediaCarouselItem]] = None
    """Per-item structure for carousel posts.

    Null for non-carousel posts. Per-item video_url is intentionally omitted (would
    be stale). For fresh video URLs, call GET /v1/raw/instagram/post/{shortcode}.
    """

    duration_seconds: Optional[float] = None
    """Video duration in seconds. Null for non-video posts."""

    thumbnail_url: Optional[str] = None
    """Thumbnail URL. For videos, this is the cover frame."""

    url: Optional[str] = None
    """Cover/primary image URL for image and carousel posts.

    Null for video posts — call GET /v1/raw/instagram/post/{shortcode} for a fresh,
    downloadable video URL. Note: returned image URLs are Instagram CDN URLs and may
    expire; a future change will migrate to persistent R2-hosted URLs.
    """


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
