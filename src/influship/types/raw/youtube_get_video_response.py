# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["YoutubeGetVideoResponse", "Data"]


class Data(BaseModel):
    availability: Optional[str] = None

    categories: List[str]

    channel_handle: Optional[str] = None

    channel_id: Optional[str] = None

    channel_name: Optional[str] = None

    comment_count: Optional[int] = None

    description: str

    duration_seconds: Optional[float] = None

    like_count: Optional[int] = None

    live_status: Optional[str] = None

    published_at: Optional[datetime] = None
    """Exact publish timestamp when supplied by YouTube, otherwise null"""

    published_date: Optional[str] = None
    """Publish date in YYYY-MM-DD format when available"""

    scraped_at: datetime

    tags: List[str]

    thumbnail_url: Optional[str] = None

    title: str

    url: str

    video_id: str

    view_count: Optional[int] = None


class YoutubeGetVideoResponse(BaseModel):
    data: Data
