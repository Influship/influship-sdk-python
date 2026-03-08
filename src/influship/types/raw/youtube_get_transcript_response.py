# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .transcript_segment import TranscriptSegment

__all__ = ["YoutubeGetTranscriptResponse", "Data"]


class Data(BaseModel):
    available_languages: List[str]
    """Available transcript languages"""

    full_text: str
    """Full transcript as plain text"""

    language: str
    """Transcript language code"""

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
