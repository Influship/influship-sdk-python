# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProfileMetrics"]


class ProfileMetrics(BaseModel):
    """Profile performance metrics"""

    avg_comments_recent: float
    """Average comments on recent posts"""

    avg_likes_recent: float
    """Average likes on recent posts"""

    avg_views_recent: Optional[float] = None
    """Average views on recent posts (for video content)"""

    engagement_rate: float
    """Engagement rate as a percentage (e.g. 3.5 means 3.5%)"""

    followers: int
    """Follower count"""

    following: int
    """Following count"""

    posts: int
    """Total post count"""

    posts_last_30d: int
    """Posts in the last 30 days"""

    posts_per_week: float
    """Average posts per week"""
