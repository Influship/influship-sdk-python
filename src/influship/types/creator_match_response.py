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
    provenance: Literal["post_evidence", "profile_fact", "inferred"]
    """How grounded a match reason is, strongest first.

    `post_evidence`: backed by a specific post you can open (see `source_post_id` /
    `evidence_quote`). `profile_fact`: backed by a stored profile fact without a
    clickable source post — weaker than post-backed. `inferred`: model reasoning
    over the profile with no direct post evidence.
    """

    text: str
    """Human-readable reason for the match"""

    evidence_quote: Optional[str] = None
    """Verbatim sentence from the source post that best supports this reason.

    Present only for `post_evidence` reasons where a genuinely supporting sentence
    exists.
    """

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
