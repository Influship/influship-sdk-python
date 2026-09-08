# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CreatorEmailLookupParams", "Creator", "CreatorCreatorEmailLookupByID", "CreatorCreatorEmailLookupByHandle"]


class CreatorEmailLookupParams(TypedDict, total=False):
    creators: Required[Iterable[Creator]]
    """Creator lookups to resolve. Response rows preserve this input order."""


class CreatorCreatorEmailLookupByID(TypedDict, total=False):
    """Creator email lookup input by creator ID"""

    creator_id: Required[str]
    """Creator profile ID to look up directly"""


class CreatorCreatorEmailLookupByHandle(TypedDict, total=False):
    """Creator email lookup input by social handle"""

    platform: Required[Literal["instagram"]]
    """Social platform for handle-based lookup"""

    username: Required[str]
    """Social username for handle-based lookup"""


Creator: TypeAlias = Union[CreatorCreatorEmailLookupByID, CreatorCreatorEmailLookupByHandle]
