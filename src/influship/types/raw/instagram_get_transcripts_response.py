# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "InstagramGetTranscriptsResponse",
    "Data",
    "DataItem",
    "DataItemInstagramTranscriptBatchSuccessItem",
    "DataItemInstagramTranscriptBatchSuccessItemData",
    "DataItemInstagramTranscriptBatchSuccessItemDataPost",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostCarouselItem",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostDisplayResource",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostEngagementVisibility",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostLocation",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostMusicAttribution",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostProductMention",
    "DataItemInstagramTranscriptBatchSuccessItemDataPostVideoVersion",
    "DataItemInstagramTranscriptBatchErrorItem",
    "DataItemInstagramTranscriptBatchErrorItemError",
]


class DataItemInstagramTranscriptBatchSuccessItemDataPostCarouselItem(BaseModel):
    display_url: str

    index: float

    is_video: bool

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None


class DataItemInstagramTranscriptBatchSuccessItemDataPostDisplayResource(BaseModel):
    config_height: float

    config_width: float

    src: str


class DataItemInstagramTranscriptBatchSuccessItemDataPostEngagementVisibility(BaseModel):
    comments_disabled: Optional[bool] = None

    like_and_view_counts_disabled: Optional[bool] = None

    viewer_can_reshare: Optional[bool] = None


class DataItemInstagramTranscriptBatchSuccessItemDataPostLocation(BaseModel):
    id: Optional[str] = None

    address_json: Optional[object] = None

    has_public_page: Optional[bool] = None

    lat: Optional[float] = None

    lng: Optional[float] = None

    name: Optional[str] = None

    slug: Optional[str] = None


class DataItemInstagramTranscriptBatchSuccessItemDataPostMusicAttribution(BaseModel):
    artist_name: Optional[str] = None

    audio_id: Optional[str] = None

    should_mute_audio: Optional[bool] = None

    song_name: Optional[str] = None

    uses_original_audio: Optional[bool] = None


class DataItemInstagramTranscriptBatchSuccessItemDataPostProductMention(BaseModel):
    merchant_username: Optional[str] = None

    product_id: Optional[str] = None

    product_name: Optional[str] = None


class DataItemInstagramTranscriptBatchSuccessItemDataPostVideoVersion(BaseModel):
    url: str

    id: Optional[str] = None

    height: Optional[float] = None

    type: Optional[float] = None

    width: Optional[float] = None


class DataItemInstagramTranscriptBatchSuccessItemDataPost(BaseModel):
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

    carousel_items: Optional[List[DataItemInstagramTranscriptBatchSuccessItemDataPostCarouselItem]] = None

    coauthor_usernames: Optional[List[str]] = None

    display_resources: Optional[List[DataItemInstagramTranscriptBatchSuccessItemDataPostDisplayResource]] = None

    engagement_visibility: Optional[DataItemInstagramTranscriptBatchSuccessItemDataPostEngagementVisibility] = None

    is_paid_partnership: Optional[bool] = None

    is_pinned: Optional[bool] = None

    location: Optional[DataItemInstagramTranscriptBatchSuccessItemDataPostLocation] = None

    music_attribution: Optional[DataItemInstagramTranscriptBatchSuccessItemDataPostMusicAttribution] = None

    owner_username: Optional[str] = None

    product_mentions: Optional[List[DataItemInstagramTranscriptBatchSuccessItemDataPostProductMention]] = None

    sponsor_usernames: Optional[List[str]] = None

    tagged_usernames: Optional[List[str]] = None

    thumbnail_url: Optional[str] = None

    video_url: Optional[str] = None

    video_versions: Optional[List[DataItemInstagramTranscriptBatchSuccessItemDataPostVideoVersion]] = None

    view_count: Optional[float] = None


class DataItemInstagramTranscriptBatchSuccessItemData(BaseModel):
    full_text: str

    language: str

    post: DataItemInstagramTranscriptBatchSuccessItemDataPost

    scraped_at: datetime

    shortcode: str

    transcript: str

    word_count: float

    duration_seconds: Optional[float] = None

    model: Optional[str] = None

    provider: Optional[str] = None


class DataItemInstagramTranscriptBatchSuccessItem(BaseModel):
    data: DataItemInstagramTranscriptBatchSuccessItemData

    shortcode: str

    success: Literal[True]


class DataItemInstagramTranscriptBatchErrorItemError(BaseModel):
    error: Literal["not_found", "private", "rate_limited", "blocked", "invalid_input", "timeout", "unknown"]

    message: str

    retry_after: Optional[float] = None

    username: Optional[str] = None


class DataItemInstagramTranscriptBatchErrorItem(BaseModel):
    error: DataItemInstagramTranscriptBatchErrorItemError

    shortcode: str

    status: float

    success: Literal[False]


DataItem: TypeAlias = Union[DataItemInstagramTranscriptBatchSuccessItem, DataItemInstagramTranscriptBatchErrorItem]


class Data(BaseModel):
    failed: float

    items: List[DataItem]

    requested: float

    scraped_at: datetime

    succeeded: float


class InstagramGetTranscriptsResponse(BaseModel):
    data: Data
