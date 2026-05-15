# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .instagram_transcript_response import InstagramTranscriptResponse

__all__ = ["InstagramGetTranscriptResponse"]


class InstagramGetTranscriptResponse(BaseModel):
    data: InstagramTranscriptResponse
