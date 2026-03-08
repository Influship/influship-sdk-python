# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TranscriptSegment"]


class TranscriptSegment(BaseModel):
    duration: float
    """Duration in seconds"""

    start: float
    """Start time in seconds"""

    text: str
    """Segment text"""
