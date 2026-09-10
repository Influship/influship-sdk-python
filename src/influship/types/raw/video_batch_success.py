# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .video_response import VideoResponse

__all__ = ["VideoBatchSuccess"]


class VideoBatchSuccess(BaseModel):
    data: VideoResponse

    success: Literal[True]

    url: str
