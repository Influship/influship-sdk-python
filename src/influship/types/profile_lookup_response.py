# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .profile_response_data import ProfileResponseData

__all__ = ["ProfileLookupResponse", "NotFound"]


class NotFound(BaseModel):
    platform: Literal["instagram"]
    """Social media platform"""

    username: str


class ProfileLookupResponse(BaseModel):
    data: List[ProfileResponseData]
    """Profiles that were found"""

    not_found: List[NotFound]
    """Profiles that were not found"""
