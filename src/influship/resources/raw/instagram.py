# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.raw import instagram_get_profile_params
from ..._base_client import make_request_options
from ...types.raw.instagram_get_profile_response import InstagramGetProfileResponse

__all__ = ["InstagramResource", "AsyncInstagramResource"]


class InstagramResource(SyncAPIResource):
    """Fetch fresh data directly from social platforms in real-time.

    Use when you need the most current information or data for profiles not yet in our database.
    """

    @cached_property
    def with_raw_response(self) -> InstagramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InstagramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstagramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return InstagramResourceWithStreamingResponse(self)

    def get_profile(
        self,
        username: str,
        *,
        include_posts: bool | Omit = omit,
        post_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetProfileResponse:
        """Fetch fresh Instagram profile data directly from Instagram in real-time.

        Use
        this when you need the most current follower counts, bio, or recent activity.

        **When to use live scraping:**

        - Profile not found in our database
        - Need real-time follower/engagement data
        - Verifying current profile status before campaign

        **Note:** Live scraping is slower than cached data (2-5 seconds) and costs more.
        Use cached endpoints when freshness isn't critical.

        **Pricing**: 0.5 credits per profile scraped ($0.005)

        Args:
          username: Username on the platform

          include_posts: Include recent posts in response

          post_limit: Number of posts to include

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/v1/raw/instagram/profile/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_posts": include_posts,
                        "post_limit": post_limit,
                    },
                    instagram_get_profile_params.InstagramGetProfileParams,
                ),
            ),
            cast_to=InstagramGetProfileResponse,
        )


class AsyncInstagramResource(AsyncAPIResource):
    """Fetch fresh data directly from social platforms in real-time.

    Use when you need the most current information or data for profiles not yet in our database.
    """

    @cached_property
    def with_raw_response(self) -> AsyncInstagramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstagramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstagramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncInstagramResourceWithStreamingResponse(self)

    async def get_profile(
        self,
        username: str,
        *,
        include_posts: bool | Omit = omit,
        post_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetProfileResponse:
        """Fetch fresh Instagram profile data directly from Instagram in real-time.

        Use
        this when you need the most current follower counts, bio, or recent activity.

        **When to use live scraping:**

        - Profile not found in our database
        - Need real-time follower/engagement data
        - Verifying current profile status before campaign

        **Note:** Live scraping is slower than cached data (2-5 seconds) and costs more.
        Use cached endpoints when freshness isn't critical.

        **Pricing**: 0.5 credits per profile scraped ($0.005)

        Args:
          username: Username on the platform

          include_posts: Include recent posts in response

          post_limit: Number of posts to include

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/v1/raw/instagram/profile/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_posts": include_posts,
                        "post_limit": post_limit,
                    },
                    instagram_get_profile_params.InstagramGetProfileParams,
                ),
            ),
            cast_to=InstagramGetProfileResponse,
        )


class InstagramResourceWithRawResponse:
    def __init__(self, instagram: InstagramResource) -> None:
        self._instagram = instagram

        self.get_profile = to_raw_response_wrapper(
            instagram.get_profile,
        )


class AsyncInstagramResourceWithRawResponse:
    def __init__(self, instagram: AsyncInstagramResource) -> None:
        self._instagram = instagram

        self.get_profile = async_to_raw_response_wrapper(
            instagram.get_profile,
        )


class InstagramResourceWithStreamingResponse:
    def __init__(self, instagram: InstagramResource) -> None:
        self._instagram = instagram

        self.get_profile = to_streamed_response_wrapper(
            instagram.get_profile,
        )


class AsyncInstagramResourceWithStreamingResponse:
    def __init__(self, instagram: AsyncInstagramResource) -> None:
        self._instagram = instagram

        self.get_profile = async_to_streamed_response_wrapper(
            instagram.get_profile,
        )
