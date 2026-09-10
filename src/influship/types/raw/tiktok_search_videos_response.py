# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .video import Video
from ..._models import BaseModel

__all__ = ["TiktokSearchVideosResponse", "Data"]


class Data(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None

    query: str

    scraped_at: datetime

    videos: List[Video]


class TiktokSearchVideosResponse(BaseModel):
    data: Data
