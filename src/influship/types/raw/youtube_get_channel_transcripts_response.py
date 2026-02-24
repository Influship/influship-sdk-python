# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["YoutubeGetChannelTranscriptsResponse", "Data", "DataItem", "DataItemTranscript"]


class DataItemTranscript(BaseModel):
    duration: float
    """Duration in seconds"""

    start: float
    """Start time in seconds"""

    text: str
    """Segment text"""


class DataItem(BaseModel):
    error: Optional[str] = None
    """Error message if transcript fetch failed for this video"""

    full_text: Optional[str] = None
    """Full transcript as plain text"""

    language: Optional[str] = None
    """Transcript language code"""

    published_text: Optional[str] = None
    """Relative publish time"""

    source: Optional[Literal["manual", "auto_generated"]] = None
    """Caption source type"""

    title: str
    """Video title"""

    transcript: Optional[List[DataItemTranscript]] = None
    """Timestamped segments (only if include_segments=true)"""

    url: str
    """Video URL"""

    video_id: str
    """YouTube video ID"""

    view_count: Optional[float] = None
    """View count"""

    word_count: Optional[float] = None
    """Word count of transcript"""


class Data(BaseModel):
    channel_id: str
    """YouTube channel ID"""

    channel_name: str
    """Channel name"""

    handle: str
    """Channel handle"""

    items: List[DataItem]
    """Per-video transcript results"""

    scraped_at: str
    """When this data was scraped"""

    transcripts_failed: int
    """Number of transcripts that failed to fetch"""

    transcripts_fetched: int
    """Number of transcripts successfully fetched"""

    videos_found: int
    """Total videos found on channel"""


class YoutubeGetChannelTranscriptsResponse(BaseModel):
    data: Data
