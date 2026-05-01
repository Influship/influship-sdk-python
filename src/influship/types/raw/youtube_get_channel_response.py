# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["YoutubeGetChannelResponse", "Data", "DataVideo"]


class DataVideo(BaseModel):
    duration_seconds: Optional[int] = None
    """Video duration in seconds"""

    duration_text: Optional[str] = None
    """Video duration text (e.g., "30:45")"""

    published_text: Optional[str] = None
    """Relative publish time as displayed by YouTube"""

    thumbnail_url: Optional[str] = None
    """Thumbnail URL"""

    title: str
    """Video title"""

    url: str
    """Video URL"""

    video_id: str
    """YouTube video ID"""

    view_count: Optional[int] = None
    """View count"""

    view_count_text: Optional[str] = None
    """View count text as displayed by YouTube"""


class Data(BaseModel):
    avatar_url: Optional[str] = None
    """Channel avatar URL"""

    banner_url: Optional[str] = None
    """Channel banner image URL"""

    channel_id: str
    """YouTube channel ID"""

    country: Optional[str] = None
    """Channel country code"""

    description: str
    """Channel description"""

    handle: Optional[str] = None
    """Channel handle (without @)"""

    keywords: List[str]
    """Channel keywords / tags"""

    name: str
    """Channel name"""

    scraped_at: datetime
    """When this data was scraped"""

    subscribers: Optional[int] = None
    """Subscriber count"""

    subscribers_text: Optional[str] = None
    """Subscriber count text as displayed by YouTube"""

    videos: List[DataVideo]
    """Recent videos (empty when include_videos=false)"""

    videos_count: Optional[int] = None
    """Total video count"""

    views_total: Optional[int] = None
    """Total view count across all videos"""


class YoutubeGetChannelResponse(BaseModel):
    data: Data
