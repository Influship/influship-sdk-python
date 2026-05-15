# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .raw_scraper_error import RawScraperError
from .instagram_single_post_response import InstagramSinglePostResponse

__all__ = [
    "InstagramGetPostsResponse",
    "Data",
    "DataItem",
    "DataItemInstagramPostBatchSuccessItem",
    "DataItemInstagramPostBatchErrorItem",
]


class DataItemInstagramPostBatchSuccessItem(BaseModel):
    data: InstagramSinglePostResponse

    shortcode: str

    success: Literal[True]


class DataItemInstagramPostBatchErrorItem(BaseModel):
    error: RawScraperError

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
