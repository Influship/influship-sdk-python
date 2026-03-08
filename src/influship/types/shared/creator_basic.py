# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CreatorBasic"]


class CreatorBasic(BaseModel):
    """Basic creator information"""

    id: str
    """Creator unique identifier"""

    avatar_url: Optional[str] = None
    """Avatar URL"""

    bio: Optional[str] = None
    """Creator bio"""

    name: str
    """Creator display name"""
