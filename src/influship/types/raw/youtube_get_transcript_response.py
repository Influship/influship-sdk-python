# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .transcript_segment import TranscriptSegment

__all__ = ["YoutubeGetTranscriptResponse", "Data", "DataAvailableLanguage"]


class DataAvailableLanguage(BaseModel):
    code: str
    """Language code (e.g., "en", "es", "en-orig")"""

    is_auto: bool
    """Whether this track is auto-generated"""

    name: str
    """Human-readable language name"""


class Data(BaseModel):
    available_languages: List[DataAvailableLanguage]
    """All caption tracks available on this video"""

    full_text: str
    """Full transcript as plain text"""

    language: str
    """Transcript language code"""

    scraped_at: datetime
    """When this data was scraped"""

    source: Literal["manual", "auto_generated"]
    """Caption source — manual subtitles or auto-generated"""

    title: str
    """Video title"""

    transcript: List[TranscriptSegment]
    """Transcript segments"""

    url: str
    """Video URL"""

    video_id: str
    """Video ID"""

    word_count: int
    """Total word count"""


class YoutubeGetTranscriptResponse(BaseModel):
    data: Data
