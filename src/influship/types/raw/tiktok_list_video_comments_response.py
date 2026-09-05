# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TiktokListVideoCommentsResponse", "Data", "DataComment", "DataCommentAuthor"]


class DataCommentAuthor(BaseModel):
    avatar_url: Optional[str] = None

    display_name: str

    is_verified: bool

    user_id: str

    username: str


class DataComment(BaseModel):
    author: DataCommentAuthor

    comment_id: str

    created_at: Optional[datetime] = None

    is_pinned: bool

    like_count: int

    reply_count: int

    text: str

    video_id: str


class Data(BaseModel):
    comments: List[DataComment]

    has_more: bool

    next_cursor: Optional[str] = None

    scraped_at: datetime

    total: Optional[int] = None

    video_id: Optional[str] = None


class TiktokListVideoCommentsResponse(BaseModel):
    data: Data
