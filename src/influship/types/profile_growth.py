# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ProfileGrowth"]


class ProfileGrowth(BaseModel):
    """Profile growth statistics"""

    followers_30d_pct: float
    """Follower growth percentage over 30 days (e.g. 2.5 means +2.5%)"""
