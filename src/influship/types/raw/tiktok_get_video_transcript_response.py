# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .transcript import Transcript

__all__ = ["TiktokGetVideoTranscriptResponse"]


class TiktokGetVideoTranscriptResponse(BaseModel):
    data: Transcript
