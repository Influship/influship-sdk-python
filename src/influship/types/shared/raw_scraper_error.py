# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RawScraperError"]


class RawScraperError(BaseModel):
    error: Literal[
        "not_found",
        "private",
        "rate_limited",
        "blocked",
        "invalid_input",
        "timeout",
        "upstream_unavailable",
        "upstream_contract_broken",
        "unknown",
    ]

    message: str

    retry_after: Optional[float] = None

    username: Optional[str] = None
