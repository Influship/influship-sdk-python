# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatorAutocompleteResponse", "Data", "DataPlatform"]


class DataPlatform(BaseModel):
    display_name: Optional[str] = None

    match_field: str
    """The field value that matched"""

    match_type: Literal["name", "username", "display_name"]
    """How the query matched this profile"""

    platform: Literal["instagram"]
    """Social media platform"""

    username: str


class Data(BaseModel):
    id: str
    """Creator ID"""

    avatar: Optional[str] = None
    """Avatar URL"""

    name: str
    """Creator name"""

    platforms: List[DataPlatform]
    """Matching platforms"""


class CreatorAutocompleteResponse(BaseModel):
    data: List[Data]
    """Autocomplete results"""
