# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "InstagramGetProfileResponse",
    "Data",
    "DataBioLink",
    "DataPost",
    "DataPostCarouselItem",
    "DataRelatedProfile",
]


class DataBioLink(BaseModel):
    title: str

    url: str

    link_type: Optional[str] = None


class DataPostCarouselItem(BaseModel):
    display_url: str

    index: float

    is_video: bool

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None


class DataPost(BaseModel):
    id: str

    caption: Optional[str] = None

    comment_count: float

    display_url: str

    is_video: bool

    like_count: float

    post_type: Literal["image", "video", "carousel"]

    shortcode: str

    taken_at: Optional[float] = None

    accessibility_caption: Optional[str] = None

    carousel_items: Optional[List[DataPostCarouselItem]] = None

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None

    view_count: Optional[float] = None


class DataRelatedProfile(BaseModel):
    full_name: Optional[str] = None

    is_private: bool

    is_verified: bool

    profile_pic_url: Optional[str] = None

    username: str


class Data(BaseModel):
    bio_links: List[DataBioLink]

    biography: str

    category_name: Optional[str] = None

    engagement_rate: float

    external_url: Optional[str] = None

    follower_count: float

    following_count: float

    full_name: str

    highlight_reel_count: float

    is_business: bool

    is_private: bool

    is_professional: bool

    is_verified: bool

    media_count: float

    posts: List[DataPost]

    profile_pic_url: str

    pronouns: List[str]

    related_profiles: List[DataRelatedProfile]

    scraped_at: datetime

    user_id: str

    username: str

    profile_pic_url_hd: Optional[str] = None


class InstagramGetProfileResponse(BaseModel):
    data: Data
