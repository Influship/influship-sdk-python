# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreatorAutocompleteResponse", "Data", "DataResult", "DataResultPlatform"]


class DataResultPlatform(BaseModel):
    display_name: Optional[str] = None

    match_field: str
    """The field value that matched"""

    match_type: Literal["name", "username", "display_name"]
    """How the query matched this profile"""

    platform: Literal["instagram"]
    """Social media platform"""

    username: str


class DataResult(BaseModel):
    id: str
    """Creator ID"""

    avatar: Optional[str] = None
    """Avatar URL"""

    name: str
    """Creator name"""

    platforms: List[DataResultPlatform]
    """Matching platforms"""


class Data(BaseModel):
    count: int
    """Number of results"""

    ok: bool

    results: List[DataResult]


class CreatorAutocompleteResponse(BaseModel):
    data: Data
