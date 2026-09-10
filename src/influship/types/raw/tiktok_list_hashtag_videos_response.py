# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .video import Video
from ..._models import BaseModel

__all__ = ["TiktokListHashtagVideosResponse", "Data"]


class Data(BaseModel):
    has_more: bool

    hashtag: str

    next_cursor: Optional[str] = None

    scraped_at: datetime

    videos: List[Video]


class TiktokListHashtagVideosResponse(BaseModel):
    data: Data
