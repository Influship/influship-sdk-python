# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.raw import (
    instagram_get_posts_params,
    instagram_get_profile_params,
    instagram_get_transcript_params,
    instagram_get_transcripts_params,
)
from ..._base_client import make_request_options
from ...types.raw.instagram_get_post_response import InstagramGetPostResponse
from ...types.raw.instagram_get_posts_response import InstagramGetPostsResponse
from ...types.raw.instagram_get_profile_response import InstagramGetProfileResponse
from ...types.raw.instagram_get_transcript_response import InstagramGetTranscriptResponse
from ...types.raw.instagram_get_transcripts_response import InstagramGetTranscriptsResponse

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

    def get_post(
        self,
        shortcode: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetPostResponse:
        """Fetch fresh Instagram post-page data by shortcode.

        This raw endpoint includes
        rich post-page fields like coauthors, tagged users, paid partnership metadata,
        product mentions, music attribution, location, display resources, and video
        versions.

        **Note:** These fields are only guaranteed on this raw single-post lookup.
        Cached post-list endpoints may not include them.

        **Pricing**: 1 credit per post scraped ($0.01)

        Args:
          shortcode: Instagram post shortcode from a /p/, /reel/, or /tv/ URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not shortcode:
            raise ValueError(f"Expected a non-empty value for `shortcode` but received {shortcode!r}")
        return self._get(
            path_template("/v1/raw/instagram/post/{shortcode}", shortcode=shortcode),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramGetPostResponse,
        )

    def get_posts(
        self,
        *,
        shortcodes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetPostsResponse:
        """Fetch fresh Instagram post-page data for a bounded list of shortcodes.

        This
        returns one item per requested shortcode with per-item success or error details.

        **Note:** Batch post lookup is capped at 20 shortcodes per request and is
        charged for every requested shortcode.

        **Pricing**: 1 credit per post scraped ($0.01)

        Args:
          shortcodes: Instagram post shortcodes from /p/, /reel/, or /tv/ URLs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/raw/instagram/posts",
            body=maybe_transform({"shortcodes": shortcodes}, instagram_get_posts_params.InstagramGetPostsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramGetPostsResponse,
        )

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

    def get_transcript(
        self,
        shortcode: str,
        *,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetTranscriptResponse:
        """
        Transcribe an Instagram video post by shortcode and return the raw post-page
        data used for transcription.

        **Pricing**: 5 credits per transcript ($0.05)

        Args:
          shortcode: Instagram post shortcode from a /p/, /reel/, or /tv/ URL

          language: Optional language code for transcription. Omit to auto-detect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not shortcode:
            raise ValueError(f"Expected a non-empty value for `shortcode` but received {shortcode!r}")
        return self._get(
            path_template("/v1/raw/instagram/transcript/{shortcode}", shortcode=shortcode),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"language": language}, instagram_get_transcript_params.InstagramGetTranscriptParams
                ),
            ),
            cast_to=InstagramGetTranscriptResponse,
        )

    def get_transcripts(
        self,
        *,
        shortcodes: SequenceNotStr[str],
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetTranscriptsResponse:
        """
        Transcribe a bounded list of Instagram video posts by shortcode and return one
        item per requested shortcode with per-item success or error details. Successful
        items include the raw post-page data used for transcription.

        **Note:** Batch transcription is capped at 10 shortcodes per request and is
        charged for every requested shortcode.

        **Pricing**: 5 credits per transcript ($0.05)

        Args:
          shortcodes: Instagram video post shortcodes from /p/, /reel/, or /tv/ URLs

          language: Optional language code for transcription. Omit to auto-detect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/raw/instagram/transcripts",
            body=maybe_transform(
                {
                    "shortcodes": shortcodes,
                    "language": language,
                },
                instagram_get_transcripts_params.InstagramGetTranscriptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramGetTranscriptsResponse,
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

    async def get_post(
        self,
        shortcode: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetPostResponse:
        """Fetch fresh Instagram post-page data by shortcode.

        This raw endpoint includes
        rich post-page fields like coauthors, tagged users, paid partnership metadata,
        product mentions, music attribution, location, display resources, and video
        versions.

        **Note:** These fields are only guaranteed on this raw single-post lookup.
        Cached post-list endpoints may not include them.

        **Pricing**: 1 credit per post scraped ($0.01)

        Args:
          shortcode: Instagram post shortcode from a /p/, /reel/, or /tv/ URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not shortcode:
            raise ValueError(f"Expected a non-empty value for `shortcode` but received {shortcode!r}")
        return await self._get(
            path_template("/v1/raw/instagram/post/{shortcode}", shortcode=shortcode),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramGetPostResponse,
        )

    async def get_posts(
        self,
        *,
        shortcodes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetPostsResponse:
        """Fetch fresh Instagram post-page data for a bounded list of shortcodes.

        This
        returns one item per requested shortcode with per-item success or error details.

        **Note:** Batch post lookup is capped at 20 shortcodes per request and is
        charged for every requested shortcode.

        **Pricing**: 1 credit per post scraped ($0.01)

        Args:
          shortcodes: Instagram post shortcodes from /p/, /reel/, or /tv/ URLs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/raw/instagram/posts",
            body=await async_maybe_transform(
                {"shortcodes": shortcodes}, instagram_get_posts_params.InstagramGetPostsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramGetPostsResponse,
        )

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

    async def get_transcript(
        self,
        shortcode: str,
        *,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetTranscriptResponse:
        """
        Transcribe an Instagram video post by shortcode and return the raw post-page
        data used for transcription.

        **Pricing**: 5 credits per transcript ($0.05)

        Args:
          shortcode: Instagram post shortcode from a /p/, /reel/, or /tv/ URL

          language: Optional language code for transcription. Omit to auto-detect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not shortcode:
            raise ValueError(f"Expected a non-empty value for `shortcode` but received {shortcode!r}")
        return await self._get(
            path_template("/v1/raw/instagram/transcript/{shortcode}", shortcode=shortcode),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, instagram_get_transcript_params.InstagramGetTranscriptParams
                ),
            ),
            cast_to=InstagramGetTranscriptResponse,
        )

    async def get_transcripts(
        self,
        *,
        shortcodes: SequenceNotStr[str],
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstagramGetTranscriptsResponse:
        """
        Transcribe a bounded list of Instagram video posts by shortcode and return one
        item per requested shortcode with per-item success or error details. Successful
        items include the raw post-page data used for transcription.

        **Note:** Batch transcription is capped at 10 shortcodes per request and is
        charged for every requested shortcode.

        **Pricing**: 5 credits per transcript ($0.05)

        Args:
          shortcodes: Instagram video post shortcodes from /p/, /reel/, or /tv/ URLs

          language: Optional language code for transcription. Omit to auto-detect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/raw/instagram/transcripts",
            body=await async_maybe_transform(
                {
                    "shortcodes": shortcodes,
                    "language": language,
                },
                instagram_get_transcripts_params.InstagramGetTranscriptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstagramGetTranscriptsResponse,
        )


class InstagramResourceWithRawResponse:
    def __init__(self, instagram: InstagramResource) -> None:
        self._instagram = instagram

        self.get_post = to_raw_response_wrapper(
            instagram.get_post,
        )
        self.get_posts = to_raw_response_wrapper(
            instagram.get_posts,
        )
        self.get_profile = to_raw_response_wrapper(
            instagram.get_profile,
        )
        self.get_transcript = to_raw_response_wrapper(
            instagram.get_transcript,
        )
        self.get_transcripts = to_raw_response_wrapper(
            instagram.get_transcripts,
        )


class AsyncInstagramResourceWithRawResponse:
    def __init__(self, instagram: AsyncInstagramResource) -> None:
        self._instagram = instagram

        self.get_post = async_to_raw_response_wrapper(
            instagram.get_post,
        )
        self.get_posts = async_to_raw_response_wrapper(
            instagram.get_posts,
        )
        self.get_profile = async_to_raw_response_wrapper(
            instagram.get_profile,
        )
        self.get_transcript = async_to_raw_response_wrapper(
            instagram.get_transcript,
        )
        self.get_transcripts = async_to_raw_response_wrapper(
            instagram.get_transcripts,
        )


class InstagramResourceWithStreamingResponse:
    def __init__(self, instagram: InstagramResource) -> None:
        self._instagram = instagram

        self.get_post = to_streamed_response_wrapper(
            instagram.get_post,
        )
        self.get_posts = to_streamed_response_wrapper(
            instagram.get_posts,
        )
        self.get_profile = to_streamed_response_wrapper(
            instagram.get_profile,
        )
        self.get_transcript = to_streamed_response_wrapper(
            instagram.get_transcript,
        )
        self.get_transcripts = to_streamed_response_wrapper(
            instagram.get_transcripts,
        )


class AsyncInstagramResourceWithStreamingResponse:
    def __init__(self, instagram: AsyncInstagramResource) -> None:
        self._instagram = instagram

        self.get_post = async_to_streamed_response_wrapper(
            instagram.get_post,
        )
        self.get_posts = async_to_streamed_response_wrapper(
            instagram.get_posts,
        )
        self.get_profile = async_to_streamed_response_wrapper(
            instagram.get_profile,
        )
        self.get_transcript = async_to_streamed_response_wrapper(
            instagram.get_transcript,
        )
        self.get_transcripts = async_to_streamed_response_wrapper(
            instagram.get_transcripts,
        )
