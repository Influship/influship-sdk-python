# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "YoutubeSearchResponse",
    "Data",
    "DataResult",
    "DataResultYouTubeSearchVideoResult",
    "DataResultYouTubeSearchChannelResult",
]


class DataResultYouTubeSearchVideoResult(BaseModel):
    channel_handle: Optional[str] = None
    """Channel handle (e.g., @username)"""

    channel_id: str
    """Channel ID"""

    channel_name: str
    """Channel name"""

    channel_verified: bool
    """Whether channel is verified"""

    description: Optional[str] = None
    """Video description snippet"""

    duration_seconds: Optional[float] = None
    """Video duration in seconds"""

    duration_text: Optional[str] = None
    """Video duration text (e.g., "12:34")"""

    published_at: Optional[str] = None
    """Approximate publish timestamp"""

    published_text: Optional[str] = None
    """Relative publish time (e.g., "2 days ago")"""

    thumbnail_url: Optional[str] = None
    """Video thumbnail URL"""

    title: str
    """Video title"""

    type: Literal["video"]

    url: str
    """Full YouTube video URL"""

    video_id: str
    """YouTube video ID"""

    view_count: Optional[float] = None
    """Number of views"""

    view_count_text: Optional[str] = None
    """View count text (e.g., "1.2M views")"""


class DataResultYouTubeSearchChannelResult(BaseModel):
    channel_handle: Optional[str] = None
    """Channel handle (e.g., @username)"""

    channel_id: str
    """Channel ID"""

    channel_name: str
    """Channel name"""

    channel_verified: bool
    """Whether channel is verified"""

    description: Optional[str] = None
    """Channel description snippet"""

    subscriber_count: Optional[float] = None
    """Subscriber count"""

    thumbnail_url: Optional[str] = None
    """Channel avatar URL"""

    type: Literal["channel"]

    url: str
    """Full YouTube channel URL"""

    video_count: Optional[int] = None
    """Number of videos on the channel"""


DataResult: TypeAlias = Union[DataResultYouTubeSearchVideoResult, DataResultYouTubeSearchChannelResult]


class Data(BaseModel):
    estimated_results: Optional[float] = None
    """Estimated total results count"""

    query: str
    """The search query"""

    results: List[DataResult]
    """Search results (videos and channels)"""

    scraped_at: str
    """When this search was performed"""


class YoutubeSearchResponse(BaseModel):
    data: Data
