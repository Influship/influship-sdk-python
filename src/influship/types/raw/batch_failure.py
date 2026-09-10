# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BatchFailure", "Error"]


class Error(BaseModel):
    code: str

    message: str


class BatchFailure(BaseModel):
    error: Error

    status: int

    success: Literal[False]

    url: str
