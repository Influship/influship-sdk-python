# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TiktokSearchUsersResponse", "Data", "DataUser"]


class DataUser(BaseModel):
    avatar_url: Optional[str] = None

    biography: Optional[str] = None

    display_name: Optional[str] = None

    follower_count: Optional[int] = None

    following_count: Optional[int] = None

    is_verified: Optional[bool] = None

    user_id: str

    username: str

    video_count: Optional[int] = None


class Data(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None

    query: str

    scraped_at: datetime

    users: List[DataUser]


class TiktokSearchUsersResponse(BaseModel):
    data: Data
