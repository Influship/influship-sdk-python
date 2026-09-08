# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .match_info import MatchInfo
from .shared.creator_basic import CreatorBasic
from .shared.profile_summary import ProfileSummary

__all__ = [
    "SearchCreateResponse",
    "Data",
    "Quality",
    "QualityUnionMember0",
    "QualityUnionMember1",
    "QualityUnionMember2",
]


class Data(BaseModel):
    creator: CreatorBasic
    """Basic creator information"""

    location_unverified: Optional[bool] = None
    """
    True when the query required a country but this creator location is unverified;
    false when the known location satisfies it; null when the query set no geography
    requirement. Known mismatches are excluded from results.
    """

    match: MatchInfo
    """Search match information"""

    primary_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""

    relevant_profile: Optional[ProfileSummary] = None
    """Abbreviated profile information"""


class QualityUnionMember0(BaseModel):
    mode: Literal["reranked"]

    reason: None = None


class QualityUnionMember1(BaseModel):
    mode: Literal["partially_reranked"]

    reason: Literal[
        "content_policy", "incomplete_rerank_output", "partial_batch_failure", "provider_error", "soft_timeout"
    ]


class QualityUnionMember2(BaseModel):
    mode: Literal["retrieval_fallback"]

    reason: Literal[
        "content_policy", "incomplete_rerank_output", "partial_batch_failure", "provider_error", "soft_timeout"
    ]


Quality: TypeAlias = Union[QualityUnionMember0, QualityUnionMember1, QualityUnionMember2]


class SearchCreateResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether more results are available"""

    next_cursor: Optional[str] = None
    """Cursor for the next page"""

    search_id: str
    """Search ID. Use with GET /v1/search/{id} for free pagination."""

    total: int
    """Total number of results across all pages"""

    quality: Optional[Quality] = None
    """
    Whether results were fully AI-reranked, partially reranked, or returned from
    retrieval fallback. Treat absence as reranked for responses from older servers
    during rolling deployment. Inspect each match.ranking_source before presenting
    its score as an AI fit score.
    """
