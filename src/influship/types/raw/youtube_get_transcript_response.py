# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["YoutubeGetTranscriptResponse", "Data", "DataTranscript"]


class DataTranscript(BaseModel):
    duration: float
    """Duration in seconds"""

    start: float
    """Start time in seconds"""

    text: str
    """Segment text"""


class Data(BaseModel):
    available_languages: List[str]
    """Available transcript languages"""

    full_text: str
    """Full transcript as plain text"""

    language: str
    """Transcript language code"""

    title: str
    """Video title"""

    transcript: List[DataTranscript]
    """Transcript segments"""

    url: str
    """Video URL"""

    video_id: str
    """Video ID"""

    word_count: int
    """Total word count"""


class YoutubeGetTranscriptResponse(BaseModel):
    data: Data
