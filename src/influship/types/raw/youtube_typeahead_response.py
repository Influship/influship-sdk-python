# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["YoutubeTypeaheadResponse", "Data"]


class Data(BaseModel):
    query: str

    scraped_at: datetime

    suggestions: List[str]


class YoutubeTypeaheadResponse(BaseModel):
    data: Data
