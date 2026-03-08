# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProfileActivity"]


class ProfileActivity(BaseModel):
    """Profile activity information"""

    last_post_at: Optional[datetime] = None
    """Timestamp of last post"""
