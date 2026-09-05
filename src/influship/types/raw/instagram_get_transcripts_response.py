# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.raw_scraper_error import RawScraperError
from .instagram_transcript_response import InstagramTranscriptResponse

__all__ = [
    "InstagramGetTranscriptsResponse",
    "Data",
    "DataItem",
    "DataItemInstagramTranscriptBatchSuccessItem",
    "DataItemInstagramTranscriptBatchErrorItem",
]


class DataItemInstagramTranscriptBatchSuccessItem(BaseModel):
    data: InstagramTranscriptResponse

    shortcode: str

    success: Literal[True]


class DataItemInstagramTranscriptBatchErrorItem(BaseModel):
    error: RawScraperError

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
