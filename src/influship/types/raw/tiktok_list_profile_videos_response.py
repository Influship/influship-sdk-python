# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .video import Video
from ..._models import BaseModel

__all__ = ["TiktokListProfileVideosResponse", "Data"]


class Data(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None

    scraped_at: datetime

    username: str

    videos: List[Video]


class TiktokListProfileVideosResponse(BaseModel):
    data: Data
