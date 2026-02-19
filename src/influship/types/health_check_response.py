# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["HealthCheckResponse"]


class HealthCheckResponse(BaseModel):
    """Health check response"""

    ok: bool
    """Service health status"""

    timestamp: datetime
    """Current server timestamp"""
