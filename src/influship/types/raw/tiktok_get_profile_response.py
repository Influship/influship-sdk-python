# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .profile import Profile
from ..._models import BaseModel

__all__ = ["TiktokGetProfileResponse"]


class TiktokGetProfileResponse(BaseModel):
    data: Profile
