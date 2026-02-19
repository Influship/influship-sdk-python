# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CreatorRetrieveParams"]


class CreatorRetrieveParams(TypedDict, total=False):
    include: str
    """Comma-separated list of additional data to include (e.g., "profiles")"""
