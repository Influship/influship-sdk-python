# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "InstagramTranscriptResponse",
    "Post",
    "PostCarouselItem",
    "PostDisplayResource",
    "PostEngagementVisibility",
    "PostLocation",
    "PostMusicAttribution",
    "PostProductMention",
    "PostVideoVersion",
]


class PostCarouselItem(BaseModel):
    display_url: str

    index: float

    is_video: bool

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None


class PostDisplayResource(BaseModel):
    config_height: float

    config_width: float

    src: str


class PostEngagementVisibility(BaseModel):
    comments_disabled: Optional[bool] = None

    like_and_view_counts_disabled: Optional[bool] = None

    viewer_can_reshare: Optional[bool] = None


class PostLocation(BaseModel):
    id: Optional[str] = None

    address_json: Optional[Dict[str, object]] = None

    has_public_page: Optional[bool] = None

    lat: Optional[float] = None

    lng: Optional[float] = None

    name: Optional[str] = None

    slug: Optional[str] = None


class PostMusicAttribution(BaseModel):
    artist_name: Optional[str] = None

    audio_id: Optional[str] = None

    should_mute_audio: Optional[bool] = None

    song_name: Optional[str] = None

    uses_original_audio: Optional[bool] = None


class PostProductMention(BaseModel):
    merchant_username: Optional[str] = None

    product_id: Optional[str] = None

    product_name: Optional[str] = None


class PostVideoVersion(BaseModel):
    url: str

    id: Optional[str] = None

    height: Optional[float] = None

    type: Optional[float] = None

    width: Optional[float] = None


class Post(BaseModel):
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

    carousel_items: Optional[List[PostCarouselItem]] = None

    coauthor_usernames: Optional[List[str]] = None

    display_resources: Optional[List[PostDisplayResource]] = None

    engagement_visibility: Optional[PostEngagementVisibility] = None

    is_paid_partnership: Optional[bool] = None

    is_pinned: Optional[bool] = None

    location: Optional[PostLocation] = None

    music_attribution: Optional[PostMusicAttribution] = None

    owner_username: Optional[str] = None

    product_mentions: Optional[List[PostProductMention]] = None

    sponsor_usernames: Optional[List[str]] = None

    tagged_usernames: Optional[List[str]] = None

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None

    video_versions: Optional[List[PostVideoVersion]] = None

    view_count: Optional[float] = None


class InstagramTranscriptResponse(BaseModel):
    full_text: str

    language: str

    post: Post

    scraped_at: datetime

    shortcode: str

    transcript: str

    word_count: float

    duration_seconds: Optional[float] = None
