# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrandSafetyAnalyzeProfilesResponse", "Data", "DataProfile", "DataSafety", "DataSafetyFlag"]


class DataProfile(BaseModel):
    id: str

    platform: Literal["instagram"]
    """Social media platform"""

    username: str


class DataSafetyFlag(BaseModel):
    """Individual brand safety flag"""

    confidence: float
    """Confidence score (0-1)"""

    description: str
    """Description of the flag"""

    severity: Literal["low", "medium", "high"]
    """Severity of the brand safety flag"""

    type: Literal[
        "profanity",
        "adult_content",
        "drugs_alcohol",
        "violence",
        "hate_speech",
        "political",
        "misinformation",
        "adult_sexual_content",
        "profanity_strong_language",
        "drugs_alcohol_tobacco",
        "violence_weapons",
        "hate_discrimination",
        "political_social_issues",
        "misinformation_conspiracy",
        "misc",
    ]
    """Type of brand safety flag"""

    evidence: Optional[List[str]] = None
    """Evidence supporting this flag"""

    examples: Optional[List[str]] = None
    """Example content that triggered this flag"""


class DataSafety(BaseModel):
    """Brand safety analysis result"""

    confidence: float
    """Confidence in the rating"""

    flags: List[DataSafetyFlag]
    """List of brand safety flags"""

    rating: Literal["A", "B", "C"]
    """Brand safety rating (A=safe, B=caution, C=avoid)"""

    summary: str
    """Human-readable summary"""


class Data(BaseModel):
    analyzed_at: datetime
    """Analysis timestamp"""

    profile: DataProfile

    safety: DataSafety
    """Brand safety analysis result"""


class BrandSafetyAnalyzeProfilesResponse(BaseModel):
    data: List[Data]
