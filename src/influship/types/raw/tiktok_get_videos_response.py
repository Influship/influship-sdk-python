# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .batch_failure import BatchFailure
from .video_batch_success import VideoBatchSuccess

__all__ = ["TiktokGetVideosResponse", "Data", "DataItem"]

DataItem: TypeAlias = Union[VideoBatchSuccess, BatchFailure]


class Data(BaseModel):
    failed: int

    items: List[DataItem]

    requested: int

    scraped_at: datetime

    succeeded: int


class TiktokGetVideosResponse(BaseModel):
    data: Data
