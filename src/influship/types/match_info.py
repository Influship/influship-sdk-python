# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MatchInfo", "Evidence"]


class Evidence(BaseModel):
    """A single evidence-grounded match reason."""

    evidence_quote: Optional[str] = None
    """
    Verbatim sentence copied from the source post caption/transcript that best
    supports this reason. Present only for `post_evidence` reasons where a genuinely
    supporting sentence exists — omitted (null) rather than filled with unrelated
    post text. Never model-generated.
    """

    fact_id: Optional[str] = None
    """Stored profile fact backing this reason, or null."""

    provenance: Literal["post_evidence", "profile_fact", "inferred"]
    """How grounded a match reason is, strongest first.

    `post_evidence`: backed by a specific post you can open (see `source_post_id` /
    `evidence_quote`). `profile_fact`: backed by a stored profile fact without a
    clickable source post — weaker than post-backed. `inferred`: model reasoning
    over the profile with no direct post evidence.
    """

    source_post_id: Optional[str] = None
    """
    Post that evidences this reason (use with GET /v1/posts/{id}), or null for
    non-post-backed reasons.
    """

    text: str
    """Human-readable reason this creator matched."""


class MatchInfo(BaseModel):
    """Search match information"""

    confidence: float
    """Rerank relevance as a 0-1 confidence. Mirrors `score`."""

    evidence: List[Evidence]
    """
    Evidence-grounded version of `reasons`, in the same order: each reason has a
    provenance label and, where it rests on a post, the backing `source_post_id` and
    a verbatim `evidence_quote`.
    """

    low_confidence: bool
    """True when `confidence` is at/below the low-confidence threshold.

    A non-breaking marker for the weak tail so you can separate "weaker matches"
    instead of treating every result as a strong match.
    """

    reasons: List[str]
    """Human-readable match reasons (plain text)."""

    score: float
    """Match relevance score (0-1)"""
