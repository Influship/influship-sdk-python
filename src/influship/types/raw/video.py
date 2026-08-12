# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Video", "Author", "Music"]


class Author(BaseModel):
    avatar_url: Optional[str] = None

    display_name: str

    is_verified: bool

    user_id: str

    username: str


class Music(BaseModel):
    author: Optional[str] = None

    duration_seconds: Optional[float] = None

    music_id: Optional[str] = None

    title: Optional[str] = None


class Video(BaseModel):
    author: Author

    comment_count: int

    created_at: Optional[datetime] = None

    description: str

    duration_seconds: Optional[float] = None

    has_watermark: Optional[bool] = None

    hashtags: List[str]

    images: List[str]

    is_pinned: bool

    like_count: int

    media_type: Literal["video", "slideshow"]

    music: Optional[Music] = None

    save_count: int

    share_count: int

    thumbnail_url: Optional[str] = None

    url: str

    video_id: str

    video_url: Optional[str] = None

    view_count: int
