# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "InstagramGetPostsResponse",
    "Data",
    "DataItem",
    "DataItemInstagramPostBatchSuccessItem",
    "DataItemInstagramPostBatchSuccessItemData",
    "DataItemInstagramPostBatchSuccessItemDataPost",
    "DataItemInstagramPostBatchSuccessItemDataPostCarouselItem",
    "DataItemInstagramPostBatchSuccessItemDataPostDisplayResource",
    "DataItemInstagramPostBatchSuccessItemDataPostEngagementVisibility",
    "DataItemInstagramPostBatchSuccessItemDataPostLocation",
    "DataItemInstagramPostBatchSuccessItemDataPostMusicAttribution",
    "DataItemInstagramPostBatchSuccessItemDataPostProductMention",
    "DataItemInstagramPostBatchSuccessItemDataPostVideoVersion",
    "DataItemInstagramPostBatchErrorItem",
    "DataItemInstagramPostBatchErrorItemError",
]


class DataItemInstagramPostBatchSuccessItemDataPostCarouselItem(BaseModel):
    display_url: str

    index: float

    is_video: bool

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None


class DataItemInstagramPostBatchSuccessItemDataPostDisplayResource(BaseModel):
    config_height: float

    config_width: float

    src: str


class DataItemInstagramPostBatchSuccessItemDataPostEngagementVisibility(BaseModel):
    comments_disabled: Optional[bool] = None

    like_and_view_counts_disabled: Optional[bool] = None

    viewer_can_reshare: Optional[bool] = None


class DataItemInstagramPostBatchSuccessItemDataPostLocation(BaseModel):
    id: Optional[str] = None

    address_json: Optional[object] = None

    has_public_page: Optional[bool] = None

    lat: Optional[float] = None

    lng: Optional[float] = None

    name: Optional[str] = None

    slug: Optional[str] = None


class DataItemInstagramPostBatchSuccessItemDataPostMusicAttribution(BaseModel):
    artist_name: Optional[str] = None

    audio_id: Optional[str] = None

    should_mute_audio: Optional[bool] = None

    song_name: Optional[str] = None

    uses_original_audio: Optional[bool] = None


class DataItemInstagramPostBatchSuccessItemDataPostProductMention(BaseModel):
    merchant_username: Optional[str] = None

    product_id: Optional[str] = None

    product_name: Optional[str] = None


class DataItemInstagramPostBatchSuccessItemDataPostVideoVersion(BaseModel):
    url: str

    id: Optional[str] = None

    height: Optional[float] = None

    type: Optional[float] = None

    width: Optional[float] = None


class DataItemInstagramPostBatchSuccessItemDataPost(BaseModel):
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

    carousel_items: Optional[List[DataItemInstagramPostBatchSuccessItemDataPostCarouselItem]] = None

    coauthor_usernames: Optional[List[str]] = None

    display_resources: Optional[List[DataItemInstagramPostBatchSuccessItemDataPostDisplayResource]] = None

    engagement_visibility: Optional[DataItemInstagramPostBatchSuccessItemDataPostEngagementVisibility] = None

    is_paid_partnership: Optional[bool] = None

    is_pinned: Optional[bool] = None

    location: Optional[DataItemInstagramPostBatchSuccessItemDataPostLocation] = None

    music_attribution: Optional[DataItemInstagramPostBatchSuccessItemDataPostMusicAttribution] = None

    owner_username: Optional[str] = None

    product_mentions: Optional[List[DataItemInstagramPostBatchSuccessItemDataPostProductMention]] = None

    sponsor_usernames: Optional[List[str]] = None

    tagged_usernames: Optional[List[str]] = None

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None

    video_versions: Optional[List[DataItemInstagramPostBatchSuccessItemDataPostVideoVersion]] = None

    view_count: Optional[float] = None


class DataItemInstagramPostBatchSuccessItemData(BaseModel):
    post: DataItemInstagramPostBatchSuccessItemDataPost

    scraped_at: datetime


class DataItemInstagramPostBatchSuccessItem(BaseModel):
    data: DataItemInstagramPostBatchSuccessItemData

    shortcode: str

    success: Literal[True]


class DataItemInstagramPostBatchErrorItemError(BaseModel):
    error: Literal["not_found", "private", "rate_limited", "blocked", "invalid_input", "timeout", "unknown"]

    message: str

    retry_after: Optional[float] = None

    username: Optional[str] = None


class DataItemInstagramPostBatchErrorItem(BaseModel):
    error: DataItemInstagramPostBatchErrorItemError

    shortcode: str

    status: float

    success: Literal[False]


DataItem: TypeAlias = Union[DataItemInstagramPostBatchSuccessItem, DataItemInstagramPostBatchErrorItem]


class Data(BaseModel):
    failed: float

    items: List[DataItem]

    requested: float

    scraped_at: datetime

    succeeded: float


class InstagramGetPostsResponse(BaseModel):
    data: Data
