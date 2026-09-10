# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .batch_failure import BatchFailure
from .transcript_batch_success import TranscriptBatchSuccess

__all__ = ["TiktokGetVideoTranscriptsResponse", "Data", "DataItem"]

DataItem: TypeAlias = Union[TranscriptBatchSuccess, BatchFailure]


class Data(BaseModel):
    failed: int

    items: List[DataItem]

    mode: Literal["auto", "captions"]

    requested: int

    scraped_at: datetime

    succeeded: int


class TiktokGetVideoTranscriptsResponse(BaseModel):
    data: Data
