# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .video import Video
from ..._models import BaseModel

__all__ = ["TiktokGetVideoResponse", "Data"]


class Data(BaseModel):
    scraped_at: datetime

    video: Video


class TiktokGetVideoResponse(BaseModel):
    data: Data
