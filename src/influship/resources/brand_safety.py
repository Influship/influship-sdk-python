# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    brand_safety_analyze_posts_params,
    brand_safety_analyze_creators_params,
    brand_safety_analyze_profiles_params,
)
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
from ..types.brand_safety_analyze_posts_response import BrandSafetyAnalyzePostsResponse
from ..types.brand_safety_analyze_creators_response import BrandSafetyAnalyzeCreatorsResponse
from ..types.brand_safety_analyze_profiles_response import BrandSafetyAnalyzeProfilesResponse

__all__ = ["BrandSafetyResource", "AsyncBrandSafetyResource"]


class BrandSafetyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandSafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BrandSafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandSafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#with_streaming_response
        """
        return BrandSafetyResourceWithStreamingResponse(self)

    def analyze_creators(
        self,
        *,
        creators: Iterable[brand_safety_analyze_creators_params.Creator],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSafetyAnalyzeCreatorsResponse:
        """
        Analyze creators for brand safety risks across all their content and profiles.
        Reviews recent posts, bio content, and historical patterns to identify potential
        issues.

        **Risk categories detected:**

        - Profanity and strong language
        - Adult/sexual content
        - Drugs, alcohol, and tobacco references
        - Violence and weapons
        - Hate speech and discrimination
        - Political and controversial topics
        - Misinformation and conspiracy content

        **Ratings:**

        - **A** - Brand safe, no significant concerns
        - **B** - Caution advised, minor or occasional issues
        - **C** - Avoid, significant brand safety risks

        **Pricing**: $0.10 per creator analyzed

        Args:
          creators: Creators to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/brand-safety/creators",
            body=maybe_transform(
                {"creators": creators}, brand_safety_analyze_creators_params.BrandSafetyAnalyzeCreatorsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSafetyAnalyzeCreatorsResponse,
        )

    def analyze_posts(
        self,
        *,
        posts: Iterable[brand_safety_analyze_posts_params.Post],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSafetyAnalyzePostsResponse:
        """Analyze specific posts for brand safety risks.

        Useful for vetting individual
        pieces of sponsored content before approval.

        **Pricing**: $0.02 per post analyzed

        Args:
          posts: Posts to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/brand-safety/posts",
            body=maybe_transform({"posts": posts}, brand_safety_analyze_posts_params.BrandSafetyAnalyzePostsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSafetyAnalyzePostsResponse,
        )

    def analyze_profiles(
        self,
        *,
        profiles: Iterable[brand_safety_analyze_profiles_params.Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSafetyAnalyzeProfilesResponse:
        """Analyze specific social media profiles for brand safety risks.

        Focuses on a
        single platform's content rather than cross-platform analysis.

        **Pricing**: $0.08 per profile analyzed

        Args:
          profiles: Profiles to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/brand-safety/profiles",
            body=maybe_transform(
                {"profiles": profiles}, brand_safety_analyze_profiles_params.BrandSafetyAnalyzeProfilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSafetyAnalyzeProfilesResponse,
        )


class AsyncBrandSafetyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandSafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandSafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandSafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inf-labs/influship-sdk-python#with_streaming_response
        """
        return AsyncBrandSafetyResourceWithStreamingResponse(self)

    async def analyze_creators(
        self,
        *,
        creators: Iterable[brand_safety_analyze_creators_params.Creator],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSafetyAnalyzeCreatorsResponse:
        """
        Analyze creators for brand safety risks across all their content and profiles.
        Reviews recent posts, bio content, and historical patterns to identify potential
        issues.

        **Risk categories detected:**

        - Profanity and strong language
        - Adult/sexual content
        - Drugs, alcohol, and tobacco references
        - Violence and weapons
        - Hate speech and discrimination
        - Political and controversial topics
        - Misinformation and conspiracy content

        **Ratings:**

        - **A** - Brand safe, no significant concerns
        - **B** - Caution advised, minor or occasional issues
        - **C** - Avoid, significant brand safety risks

        **Pricing**: $0.10 per creator analyzed

        Args:
          creators: Creators to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/brand-safety/creators",
            body=await async_maybe_transform(
                {"creators": creators}, brand_safety_analyze_creators_params.BrandSafetyAnalyzeCreatorsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSafetyAnalyzeCreatorsResponse,
        )

    async def analyze_posts(
        self,
        *,
        posts: Iterable[brand_safety_analyze_posts_params.Post],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSafetyAnalyzePostsResponse:
        """Analyze specific posts for brand safety risks.

        Useful for vetting individual
        pieces of sponsored content before approval.

        **Pricing**: $0.02 per post analyzed

        Args:
          posts: Posts to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/brand-safety/posts",
            body=await async_maybe_transform(
                {"posts": posts}, brand_safety_analyze_posts_params.BrandSafetyAnalyzePostsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSafetyAnalyzePostsResponse,
        )

    async def analyze_profiles(
        self,
        *,
        profiles: Iterable[brand_safety_analyze_profiles_params.Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSafetyAnalyzeProfilesResponse:
        """Analyze specific social media profiles for brand safety risks.

        Focuses on a
        single platform's content rather than cross-platform analysis.

        **Pricing**: $0.08 per profile analyzed

        Args:
          profiles: Profiles to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/brand-safety/profiles",
            body=await async_maybe_transform(
                {"profiles": profiles}, brand_safety_analyze_profiles_params.BrandSafetyAnalyzeProfilesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandSafetyAnalyzeProfilesResponse,
        )


class BrandSafetyResourceWithRawResponse:
    def __init__(self, brand_safety: BrandSafetyResource) -> None:
        self._brand_safety = brand_safety

        self.analyze_creators = to_raw_response_wrapper(
            brand_safety.analyze_creators,
        )
        self.analyze_posts = to_raw_response_wrapper(
            brand_safety.analyze_posts,
        )
        self.analyze_profiles = to_raw_response_wrapper(
            brand_safety.analyze_profiles,
        )


class AsyncBrandSafetyResourceWithRawResponse:
    def __init__(self, brand_safety: AsyncBrandSafetyResource) -> None:
        self._brand_safety = brand_safety

        self.analyze_creators = async_to_raw_response_wrapper(
            brand_safety.analyze_creators,
        )
        self.analyze_posts = async_to_raw_response_wrapper(
            brand_safety.analyze_posts,
        )
        self.analyze_profiles = async_to_raw_response_wrapper(
            brand_safety.analyze_profiles,
        )


class BrandSafetyResourceWithStreamingResponse:
    def __init__(self, brand_safety: BrandSafetyResource) -> None:
        self._brand_safety = brand_safety

        self.analyze_creators = to_streamed_response_wrapper(
            brand_safety.analyze_creators,
        )
        self.analyze_posts = to_streamed_response_wrapper(
            brand_safety.analyze_posts,
        )
        self.analyze_profiles = to_streamed_response_wrapper(
            brand_safety.analyze_profiles,
        )


class AsyncBrandSafetyResourceWithStreamingResponse:
    def __init__(self, brand_safety: AsyncBrandSafetyResource) -> None:
        self._brand_safety = brand_safety

        self.analyze_creators = async_to_streamed_response_wrapper(
            brand_safety.analyze_creators,
        )
        self.analyze_posts = async_to_streamed_response_wrapper(
            brand_safety.analyze_posts,
        )
        self.analyze_profiles = async_to_streamed_response_wrapper(
            brand_safety.analyze_profiles,
        )
