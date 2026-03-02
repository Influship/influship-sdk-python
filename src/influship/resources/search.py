# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import search_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.search_create_response import SearchCreateResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/influship/influship-sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        filters: search_create_params.Filters | Omit = omit,
        limit: int | Omit = omit,
        platforms: List[Literal["instagram"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchCreateResponse:
        """Search for creators using natural language queries.

        The AI understands intent
        and context to match creators based on content themes, audience demographics,
        and style.

        **Use cases:**

        - Find creators in a specific niche ("vegan food bloggers in LA")
        - Discover creators with specific audience characteristics ("fitness influencers
          with millennial audience")
        - Search by content style ("creators who post cinematic travel videos")

        **Pricing**: 25 credits base + 2 credits per creator returned

        Args:
          query: Natural language search query

          cursor: Pagination cursor for next page

          filters: Additional filters

          limit: Maximum results to return

          platforms: Filter results to specific platforms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/search",
            body=maybe_transform(
                {
                    "query": query,
                    "cursor": cursor,
                    "filters": filters,
                    "limit": limit,
                    "platforms": platforms,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchCreateResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/influship/influship-sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        filters: search_create_params.Filters | Omit = omit,
        limit: int | Omit = omit,
        platforms: List[Literal["instagram"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchCreateResponse:
        """Search for creators using natural language queries.

        The AI understands intent
        and context to match creators based on content themes, audience demographics,
        and style.

        **Use cases:**

        - Find creators in a specific niche ("vegan food bloggers in LA")
        - Discover creators with specific audience characteristics ("fitness influencers
          with millennial audience")
        - Search by content style ("creators who post cinematic travel videos")

        **Pricing**: 25 credits base + 2 credits per creator returned

        Args:
          query: Natural language search query

          cursor: Pagination cursor for next page

          filters: Additional filters

          limit: Maximum results to return

          platforms: Filter results to specific platforms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "cursor": cursor,
                    "filters": filters,
                    "limit": limit,
                    "platforms": platforms,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchCreateResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_raw_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_raw_response_wrapper(
            search.create,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_streamed_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_streamed_response_wrapper(
            search.create,
        )
