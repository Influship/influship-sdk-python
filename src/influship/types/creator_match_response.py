# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatorMatchResponse", "Data", "DataCreator", "DataInput", "DataMatch"]


class DataCreator(BaseModel):
    id: str

    avatar_url: Optional[str] = None

    name: str


class DataInput(BaseModel):
    creator_id: Optional[str] = None

    platform: Optional[Literal["instagram"]] = None
    """Social media platform"""

    username: Optional[str] = None


class DataMatch(BaseModel):
    decision: Literal["good", "neutral", "avoid"]
    """Match decision recommendation"""

    evidence: List[str]
    """Evidence supporting the decision"""

    explanation: str
    """Human-readable explanation"""

    score: float
    """Match score (0-1)"""


class Data(BaseModel):
    creator: DataCreator

    input: DataInput

    match: DataMatch


class CreatorMatchResponse(BaseModel):
    data: List[Data]
