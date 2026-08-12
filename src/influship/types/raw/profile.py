# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Profile"]


class Profile(BaseModel):
    avatar_url: Optional[str] = None

    biography: str

    display_name: str

    external_url: Optional[str] = None

    follower_count: int

    following_count: int

    is_business: bool

    is_private: bool

    is_verified: bool

    like_count: int

    profile_url: str

    scraped_at: datetime

    user_id: str

    username: str

    video_count: int
