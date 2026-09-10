# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .video_response import VideoResponse

__all__ = ["TiktokGetVideoResponse"]


class TiktokGetVideoResponse(BaseModel):
    data: VideoResponse
