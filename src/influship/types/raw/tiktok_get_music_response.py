# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TiktokGetMusicResponse", "Data"]


class Data(BaseModel):
    album: Optional[str] = None

    author: Optional[str] = None

    cover_url: Optional[str] = None
    """Temporary upstream cover URL; availability and expiry are not guaranteed"""

    duration_seconds: Optional[int] = None

    music_id: str

    play_url: Optional[str] = None
    """Temporary upstream audio URL; not a durable download or a usage licence"""

    scraped_at: datetime

    title: Optional[str] = None

    video_count: Optional[int] = None
    """Observed number of videos using this sound; null when unavailable"""


class TiktokGetMusicResponse(BaseModel):
    data: Data
