# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import creator_email_lookup_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.creator_email_lookup_response import CreatorEmailLookupResponse

__all__ = ["CreatorEmailsResource", "AsyncCreatorEmailsResource"]


class CreatorEmailsResource(SyncAPIResource):
    """Look up known creator email addresses by creator ID or social username.

    Empty or unresolved results are not billable.
    """

    @cached_property
    def with_raw_response(self) -> CreatorEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CreatorEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreatorEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return CreatorEmailsResourceWithStreamingResponse(self)

    def lookup(
        self,
        *,
        creators: Iterable[creator_email_lookup_params.Creator],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorEmailLookupResponse:
        """
        Look up known email addresses for creators by creator ID or social username.

        **Billing behavior:**

        - Charged only for unique resolved creators with at least one returned email
        - Empty and unresolved results are not billable
        - Returns validation status so unvalidated emails are explicit

        **Pricing**: 5 credits per creator with at least one returned email ($0.05)

        Args:
          creators: Creator lookups to resolve. Response rows preserve this input order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/creator-emails/lookup",
            body=maybe_transform({"creators": creators}, creator_email_lookup_params.CreatorEmailLookupParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatorEmailLookupResponse,
        )


class AsyncCreatorEmailsResource(AsyncAPIResource):
    """Look up known creator email addresses by creator ID or social username.

    Empty or unresolved results are not billable.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCreatorEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreatorEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreatorEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncCreatorEmailsResourceWithStreamingResponse(self)

    async def lookup(
        self,
        *,
        creators: Iterable[creator_email_lookup_params.Creator],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorEmailLookupResponse:
        """
        Look up known email addresses for creators by creator ID or social username.

        **Billing behavior:**

        - Charged only for unique resolved creators with at least one returned email
        - Empty and unresolved results are not billable
        - Returns validation status so unvalidated emails are explicit

        **Pricing**: 5 credits per creator with at least one returned email ($0.05)

        Args:
          creators: Creator lookups to resolve. Response rows preserve this input order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/creator-emails/lookup",
            body=await async_maybe_transform(
                {"creators": creators}, creator_email_lookup_params.CreatorEmailLookupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatorEmailLookupResponse,
        )


class CreatorEmailsResourceWithRawResponse:
    def __init__(self, creator_emails: CreatorEmailsResource) -> None:
        self._creator_emails = creator_emails

        self.lookup = to_raw_response_wrapper(
            creator_emails.lookup,
        )


class AsyncCreatorEmailsResourceWithRawResponse:
    def __init__(self, creator_emails: AsyncCreatorEmailsResource) -> None:
        self._creator_emails = creator_emails

        self.lookup = async_to_raw_response_wrapper(
            creator_emails.lookup,
        )


class CreatorEmailsResourceWithStreamingResponse:
    def __init__(self, creator_emails: CreatorEmailsResource) -> None:
        self._creator_emails = creator_emails

        self.lookup = to_streamed_response_wrapper(
            creator_emails.lookup,
        )


class AsyncCreatorEmailsResourceWithStreamingResponse:
    def __init__(self, creator_emails: AsyncCreatorEmailsResource) -> None:
        self._creator_emails = creator_emails

        self.lookup = async_to_streamed_response_wrapper(
            creator_emails.lookup,
        )
