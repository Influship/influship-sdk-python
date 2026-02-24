# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["YoutubeGetChannelResponse", "Data", "DataVideo"]


class DataVideo(BaseModel):
    id: str
    """Video ID"""

    comments: Optional[int] = None
    """Comment count"""

    duration_seconds: Optional[int] = None
    """Video duration in seconds"""

    likes: Optional[int] = None
    """Like count"""

    published_at: datetime
    """Publish timestamp"""

    thumbnail_url: Optional[str] = None
    """Thumbnail URL"""

    title: str
    """Video title"""

    url: str
    """Video URL"""

    views: Optional[int] = None
    """View count"""


class Data(BaseModel):
    avatar_url: Optional[str] = None
    """Channel avatar URL"""

    description: Optional[str] = None
    """Channel description"""

    handle: str
    """Channel handle"""

    name: str
    """Channel name"""

    scraped_at: datetime
    """When this data was scraped"""

    subscribers: int
    """Subscriber count"""

    videos_count: int
    """Total video count"""

    views_total: int
    """Total view count"""

    videos: Optional[List[DataVideo]] = None
    """Recent videos (only included when include_videos=true)"""


class YoutubeGetChannelResponse(BaseModel):
    data: Data
