# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.profile_summary import ProfileSummary

__all__ = ["CreatorRetrieveResponse", "Data"]


class Data(BaseModel):
    """Full creator details"""

    id: str
    """Creator unique identifier"""

    ai_summary: Optional[str] = None
    """AI-generated summary of the creator"""

    audience_demographics: Optional[str] = None
    """Synthesized audience demographic summary"""

    avatar_url: Optional[str] = None
    """Avatar URL"""

    bio: Optional[str] = None
    """Creator bio"""

    brand_alignment: List[str]
    """Brand categories this creator is likely to align with"""

    content_themes: List[str]
    """Content themes/topics"""

    key_facts: List[str]
    """Synthesized facts and notable context about the creator"""

    name: str
    """Creator display name"""

    vibe_and_aesthetics: Optional[str] = None
    """Synthesized description of visual style and tone"""

    profiles: Optional[List[ProfileSummary]] = None
    """Social profiles (only included when include=profiles)"""


class CreatorRetrieveResponse(BaseModel):
    data: Data
    """Full creator details"""

    warning: Optional[str] = None
    """
    Present when partial results were returned because one or more linked profiles
    were skipped for data integrity reasons.
    """
