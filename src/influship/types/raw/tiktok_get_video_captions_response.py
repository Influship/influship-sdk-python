# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TiktokGetVideoCaptionsResponse", "Data", "DataSegment"]


class DataSegment(BaseModel):
    end_ms: int

    start_ms: int

    text: str


class Data(BaseModel):
    duration_seconds: Optional[float] = None

    full_text: str

    language: str

    scraped_at: datetime

    segments: List[DataSegment]

    source: Literal["captions"]

    transcript: str

    url: str

    video_id: str

    word_count: int


class TiktokGetVideoCaptionsResponse(BaseModel):
    data: Data
