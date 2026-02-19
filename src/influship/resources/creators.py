# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import creator_match_params, creator_retrieve_params, creator_lookalike_params, creator_autocomplete_params
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
from ..types.creator_match_response import CreatorMatchResponse
from ..types.creator_retrieve_response import CreatorRetrieveResponse
from ..types.creator_lookalike_response import CreatorLookalikeResponse
from ..types.creator_autocomplete_response import CreatorAutocompleteResponse

__all__ = ["CreatorsResource", "AsyncCreatorsResource"]


class CreatorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CreatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#with_streaming_response
        """
        return CreatorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        include: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorRetrieveResponse:
        """
        Retrieve a creator's profile including AI-generated summary, content themes, and
        optionally their linked social profiles.

        **What is a Creator?** A creator is a cross-platform entity representing a
        person or brand. They may have profiles on multiple social networks (Instagram,
        YouTube, TikTok, etc.) that are linked together.

        **Include options:**

        - `profiles`: Include all linked social profiles with metrics

        **Pricing**: Free (included in your plan)

        Args:
          id: Creator unique identifier

          include: Comma-separated list of additional data to include (e.g., "profiles")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/creators/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, creator_retrieve_params.CreatorRetrieveParams),
            ),
            cast_to=CreatorRetrieveResponse,
        )

    def autocomplete(
        self,
        *,
        q: str,
        limit: str | Omit = omit,
        platform: Literal["instagram"] | Omit = omit,
        scope: Literal["creator_only", "matched_platforms", "all_platforms"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorAutocompleteResponse:
        """Fast typeahead search for creators by name or username.

        Optimized for
        search-as-you-type UIs with sub-100ms response times.

        **Matching behavior:**

        - Matches against creator name, username, and display name
        - Results include which field matched and the matching value
        - Prefix matching (e.g., "fit" matches "fitness_coach")

        **Scope options:**

        - `creator_only`: Return only the creator entity
        - `matched_platforms`: Return only profiles that matched the query
        - `all_platforms`: Return all linked profiles (default)

        **Pricing**: Free (included in your plan)

        Args:
          q: Search query (min 2 characters)

          limit: Maximum results to return

          platform: Filter by platform

          scope: Which platforms to include in results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/creators/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "platform": platform,
                        "scope": scope,
                    },
                    creator_autocomplete_params.CreatorAutocompleteParams,
                ),
            ),
            cast_to=CreatorAutocompleteResponse,
        )

    def lookalike(
        self,
        *,
        seeds: Iterable[creator_lookalike_params.Seed],
        cursor: str | Omit = omit,
        filters: creator_lookalike_params.Filters | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorLookalikeResponse:
        """
        Find creators similar to provided seed creators using AI-powered similarity
        matching. Analyzes content themes, audience overlap, posting style, and
        engagement patterns.

        **Use cases:**

        - Expand campaigns with creators similar to proven performers
        - Find alternatives when preferred creators are unavailable
        - Discover emerging creators in the same niche

        **How it works:**

        1. Provide 1-10 seed creators (by ID or platform/username)
        2. Optionally weight seeds to prioritize certain creators
        3. Get ranked results with similarity scores and shared traits

        **Pricing**: $0.02 per creator returned

        Args:
          seeds: Seed creators to find similar creators for

          cursor: Pagination cursor for next page

          filters: Additional filters

          limit: Maximum results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/creators/lookalike",
            body=maybe_transform(
                {
                    "seeds": seeds,
                    "cursor": cursor,
                    "filters": filters,
                    "limit": limit,
                },
                creator_lookalike_params.CreatorLookalikeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatorLookalikeResponse,
        )

    def match(
        self,
        *,
        creators: Iterable[creator_match_params.Creator],
        intent: creator_match_params.Intent,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorMatchResponse:
        """Evaluate how well creators match a specific campaign using AI analysis.

        Returns
        a fit score (0-1), decision recommendation (good/neutral/avoid), and
        evidence-based explanations.

        **Use cases:**

        - Vet shortlisted creators before outreach
        - Rank candidates for a specific campaign
        - Get AI-generated talking points for why a creator fits

        **How it works:**

        1. Describe your campaign intent and target audience
        2. Provide up to 100 creators to evaluate
        3. Get detailed scores with explanations and evidence

        **Pricing**: $0.05 per creator evaluated

        Args:
          creators: Creators to evaluate

          intent: Campaign intent for creator matching

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/creators/match",
            body=maybe_transform(
                {
                    "creators": creators,
                    "intent": intent,
                },
                creator_match_params.CreatorMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatorMatchResponse,
        )


class AsyncCreatorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#with_streaming_response
        """
        return AsyncCreatorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        include: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorRetrieveResponse:
        """
        Retrieve a creator's profile including AI-generated summary, content themes, and
        optionally their linked social profiles.

        **What is a Creator?** A creator is a cross-platform entity representing a
        person or brand. They may have profiles on multiple social networks (Instagram,
        YouTube, TikTok, etc.) that are linked together.

        **Include options:**

        - `profiles`: Include all linked social profiles with metrics

        **Pricing**: Free (included in your plan)

        Args:
          id: Creator unique identifier

          include: Comma-separated list of additional data to include (e.g., "profiles")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/creators/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, creator_retrieve_params.CreatorRetrieveParams),
            ),
            cast_to=CreatorRetrieveResponse,
        )

    async def autocomplete(
        self,
        *,
        q: str,
        limit: str | Omit = omit,
        platform: Literal["instagram"] | Omit = omit,
        scope: Literal["creator_only", "matched_platforms", "all_platforms"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorAutocompleteResponse:
        """Fast typeahead search for creators by name or username.

        Optimized for
        search-as-you-type UIs with sub-100ms response times.

        **Matching behavior:**

        - Matches against creator name, username, and display name
        - Results include which field matched and the matching value
        - Prefix matching (e.g., "fit" matches "fitness_coach")

        **Scope options:**

        - `creator_only`: Return only the creator entity
        - `matched_platforms`: Return only profiles that matched the query
        - `all_platforms`: Return all linked profiles (default)

        **Pricing**: Free (included in your plan)

        Args:
          q: Search query (min 2 characters)

          limit: Maximum results to return

          platform: Filter by platform

          scope: Which platforms to include in results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/creators/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "platform": platform,
                        "scope": scope,
                    },
                    creator_autocomplete_params.CreatorAutocompleteParams,
                ),
            ),
            cast_to=CreatorAutocompleteResponse,
        )

    async def lookalike(
        self,
        *,
        seeds: Iterable[creator_lookalike_params.Seed],
        cursor: str | Omit = omit,
        filters: creator_lookalike_params.Filters | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorLookalikeResponse:
        """
        Find creators similar to provided seed creators using AI-powered similarity
        matching. Analyzes content themes, audience overlap, posting style, and
        engagement patterns.

        **Use cases:**

        - Expand campaigns with creators similar to proven performers
        - Find alternatives when preferred creators are unavailable
        - Discover emerging creators in the same niche

        **How it works:**

        1. Provide 1-10 seed creators (by ID or platform/username)
        2. Optionally weight seeds to prioritize certain creators
        3. Get ranked results with similarity scores and shared traits

        **Pricing**: $0.02 per creator returned

        Args:
          seeds: Seed creators to find similar creators for

          cursor: Pagination cursor for next page

          filters: Additional filters

          limit: Maximum results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/creators/lookalike",
            body=await async_maybe_transform(
                {
                    "seeds": seeds,
                    "cursor": cursor,
                    "filters": filters,
                    "limit": limit,
                },
                creator_lookalike_params.CreatorLookalikeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatorLookalikeResponse,
        )

    async def match(
        self,
        *,
        creators: Iterable[creator_match_params.Creator],
        intent: creator_match_params.Intent,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatorMatchResponse:
        """Evaluate how well creators match a specific campaign using AI analysis.

        Returns
        a fit score (0-1), decision recommendation (good/neutral/avoid), and
        evidence-based explanations.

        **Use cases:**

        - Vet shortlisted creators before outreach
        - Rank candidates for a specific campaign
        - Get AI-generated talking points for why a creator fits

        **How it works:**

        1. Describe your campaign intent and target audience
        2. Provide up to 100 creators to evaluate
        3. Get detailed scores with explanations and evidence

        **Pricing**: $0.05 per creator evaluated

        Args:
          creators: Creators to evaluate

          intent: Campaign intent for creator matching

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/creators/match",
            body=await async_maybe_transform(
                {
                    "creators": creators,
                    "intent": intent,
                },
                creator_match_params.CreatorMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatorMatchResponse,
        )


class CreatorsResourceWithRawResponse:
    def __init__(self, creators: CreatorsResource) -> None:
        self._creators = creators

        self.retrieve = to_raw_response_wrapper(
            creators.retrieve,
        )
        self.autocomplete = to_raw_response_wrapper(
            creators.autocomplete,
        )
        self.lookalike = to_raw_response_wrapper(
            creators.lookalike,
        )
        self.match = to_raw_response_wrapper(
            creators.match,
        )


class AsyncCreatorsResourceWithRawResponse:
    def __init__(self, creators: AsyncCreatorsResource) -> None:
        self._creators = creators

        self.retrieve = async_to_raw_response_wrapper(
            creators.retrieve,
        )
        self.autocomplete = async_to_raw_response_wrapper(
            creators.autocomplete,
        )
        self.lookalike = async_to_raw_response_wrapper(
            creators.lookalike,
        )
        self.match = async_to_raw_response_wrapper(
            creators.match,
        )


class CreatorsResourceWithStreamingResponse:
    def __init__(self, creators: CreatorsResource) -> None:
        self._creators = creators

        self.retrieve = to_streamed_response_wrapper(
            creators.retrieve,
        )
        self.autocomplete = to_streamed_response_wrapper(
            creators.autocomplete,
        )
        self.lookalike = to_streamed_response_wrapper(
            creators.lookalike,
        )
        self.match = to_streamed_response_wrapper(
            creators.match,
        )


class AsyncCreatorsResourceWithStreamingResponse:
    def __init__(self, creators: AsyncCreatorsResource) -> None:
        self._creators = creators

        self.retrieve = async_to_streamed_response_wrapper(
            creators.retrieve,
        )
        self.autocomplete = async_to_streamed_response_wrapper(
            creators.autocomplete,
        )
        self.lookalike = async_to_streamed_response_wrapper(
            creators.lookalike,
        )
        self.match = async_to_streamed_response_wrapper(
            creators.match,
        )
