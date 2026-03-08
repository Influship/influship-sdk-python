# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .profile_response_data import ProfileResponseData

__all__ = ["ProfileGetResponse"]


class ProfileGetResponse(BaseModel):
    data: ProfileResponseData
    """Full profile details"""

    warning: Optional[str] = None
    """
    Present when partial results were returned because profile metrics/data were
    skipped due to integrity issues.
    """
