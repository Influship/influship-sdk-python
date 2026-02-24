# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatorMatchResponse", "Data", "DataCreator", "DataInput", "DataMatch", "DataMatchReason"]


class DataCreator(BaseModel):
    id: str

    avatar_url: Optional[str] = None

    name: str


class DataInput(BaseModel):
    creator_id: Optional[str] = None

    platform: Optional[Literal["instagram"]] = None
    """Social media platform"""

    username: Optional[str] = None


class DataMatchReason(BaseModel):
    text: str
    """Human-readable reason for the match"""

    fact_id: Optional[str] = None
    """ID of the supporting fact, if applicable"""

    source_post_id: Optional[str] = None
    """ID of the source post, if applicable"""


class DataMatch(BaseModel):
    decision: Literal["good", "neutral", "avoid"]
    """Match decision recommendation"""

    reasons: List[DataMatchReason]
    """Structured reasons supporting the decision"""

    score: float
    """Match score (0-1)"""


class Data(BaseModel):
    creator: DataCreator

    input: DataInput

    match: DataMatch


class CreatorMatchResponse(BaseModel):
    data: List[Data]
