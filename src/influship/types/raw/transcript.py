# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Transcript", "Segment"]


class Segment(BaseModel):
    end_ms: int

    start_ms: int

    text: str


class Transcript(BaseModel):
    duration_seconds: Optional[float] = None

    full_text: str

    language: str

    scraped_at: datetime

    segments: List[Segment]

    source: Literal["captions", "generated"]

    transcript: str

    url: str

    video_id: str

    word_count: int
