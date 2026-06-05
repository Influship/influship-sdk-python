# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "CreatorEmailLookupResponse",
    "Data",
    "DataBilling",
    "DataResult",
    "DataResultEmail",
    "DataResultInput",
    "DataResultInputCreatorEmailLookupByIDOutput",
    "DataResultInputCreatorEmailLookupByHandleOutput",
]


class DataBilling(BaseModel):
    """Creator email lookup billing summary"""

    billable_results: int
    """Unique resolved creators with at least one returned email"""

    credits_charged: float
    """Preview of credits charged for this lookup"""


class DataResultEmail(BaseModel):
    """API-visible creator email"""

    confidence: Optional[float] = None
    """Nullable confidence score for the email"""

    email: str
    """Email address as stored, preserving original casing"""

    first_seen_at: datetime
    """When Influship first observed this email"""

    is_primary: bool
    """Whether this is the primary email for the creator"""

    last_seen_at: datetime
    """When Influship most recently observed this email"""

    status: Literal["unvalidated", "valid", "risky", "creator_verified"]
    """API-visible email validation status"""

    validated_at: Optional[datetime] = None
    """When the email was last validated, if known"""


class DataResultInputCreatorEmailLookupByIDOutput(BaseModel):
    """Creator email lookup input by creator ID"""

    creator_id: str
    """Creator profile ID to look up directly"""


class DataResultInputCreatorEmailLookupByHandleOutput(BaseModel):
    """Creator email lookup input by social handle"""

    platform: Literal["instagram"]
    """Social platform for handle-based lookup"""

    username: str
    """Social username for handle-based lookup"""


DataResultInput: TypeAlias = Union[
    DataResultInputCreatorEmailLookupByIDOutput, DataResultInputCreatorEmailLookupByHandleOutput
]


class DataResult(BaseModel):
    """Creator email lookup result"""

    creator_id: Optional[str] = None
    """Resolved creator ID, or null when the input could not be resolved"""

    emails: List[DataResultEmail]
    """API-visible emails for the resolved creator. Empty results are not billable."""

    input: DataResultInput
    """Creator email lookup input by creator ID or social handle"""

    resolved: bool
    """Whether the lookup resolved to a creator profile"""


class Data(BaseModel):
    billing: DataBilling
    """Creator email lookup billing summary"""

    results: List[DataResult]


class CreatorEmailLookupResponse(BaseModel):
    """Creator email lookup response"""

    data: Data
