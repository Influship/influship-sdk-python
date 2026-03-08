# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import profile_lookup_params
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
from ..types.profile_get_response import ProfileGetResponse
from ..types.profile_lookup_response import ProfileLookupResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    """
    Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
    """

    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def get(
        self,
        username: str,
        *,
        platform: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileGetResponse:
        """
        Retrieve detailed profile data including metrics, growth statistics, and
        activity information from our database.

        **Response includes:**

        - Basic info (bio, avatar, verification status)
        - Performance metrics (followers, engagement rate, avg likes/comments)
        - Growth data (30-day follower growth, monthly rate)
        - Activity data (last post date, posting frequency)

        **Pricing**: 0.1 credits per request ($0.001)

        Args:
          platform: Platform name

          username: Username on the platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not platform:
            raise ValueError(f"Expected a non-empty value for `platform` but received {platform!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/v1/profiles/{platform}/{username}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileGetResponse,
        )

    def lookup(
        self,
        *,
        profiles: Iterable[profile_lookup_params.Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileLookupResponse:
        """Look up multiple profiles in a single request.

        Efficiently retrieve data for up
        to 100 profiles at once.

        **Response includes:**

        - `found`: Array of profiles that exist in our database
        - `not_found`: Array of profiles that weren't found (consider live scraping
          these)

        **Pricing**: 0.1 credits per profile ($0.001)

        Args:
          profiles: Profiles to lookup

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/profiles/lookup",
            body=maybe_transform({"profiles": profiles}, profile_lookup_params.ProfileLookupParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileLookupResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    """
    Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
    """

    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def get(
        self,
        username: str,
        *,
        platform: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileGetResponse:
        """
        Retrieve detailed profile data including metrics, growth statistics, and
        activity information from our database.

        **Response includes:**

        - Basic info (bio, avatar, verification status)
        - Performance metrics (followers, engagement rate, avg likes/comments)
        - Growth data (30-day follower growth, monthly rate)
        - Activity data (last post date, posting frequency)

        **Pricing**: 0.1 credits per request ($0.001)

        Args:
          platform: Platform name

          username: Username on the platform

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not platform:
            raise ValueError(f"Expected a non-empty value for `platform` but received {platform!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/v1/profiles/{platform}/{username}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileGetResponse,
        )

    async def lookup(
        self,
        *,
        profiles: Iterable[profile_lookup_params.Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileLookupResponse:
        """Look up multiple profiles in a single request.

        Efficiently retrieve data for up
        to 100 profiles at once.

        **Response includes:**

        - `found`: Array of profiles that exist in our database
        - `not_found`: Array of profiles that weren't found (consider live scraping
          these)

        **Pricing**: 0.1 credits per profile ($0.001)

        Args:
          profiles: Profiles to lookup

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/profiles/lookup",
            body=await async_maybe_transform({"profiles": profiles}, profile_lookup_params.ProfileLookupParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileLookupResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.get = to_raw_response_wrapper(
            profiles.get,
        )
        self.lookup = to_raw_response_wrapper(
            profiles.lookup,
        )


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.get = async_to_raw_response_wrapper(
            profiles.get,
        )
        self.lookup = async_to_raw_response_wrapper(
            profiles.lookup,
        )


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.get = to_streamed_response_wrapper(
            profiles.get,
        )
        self.lookup = to_streamed_response_wrapper(
            profiles.lookup,
        )


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.get = async_to_streamed_response_wrapper(
            profiles.get,
        )
        self.lookup = async_to_streamed_response_wrapper(
            profiles.lookup,
        )
