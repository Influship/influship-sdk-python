# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .transcript import Transcript

__all__ = ["TranscriptBatchSuccess"]


class TranscriptBatchSuccess(BaseModel):
    data: Transcript

    success: Literal[True]

    url: str
