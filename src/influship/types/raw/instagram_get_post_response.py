# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .instagram_single_post_response import InstagramSinglePostResponse

__all__ = ["InstagramGetPostResponse"]


class InstagramGetPostResponse(BaseModel):
    data: InstagramSinglePostResponse
