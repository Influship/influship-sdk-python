# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.raw import (
    tiktok_get_video_params,
    tiktok_list_profile_videos_params,
    tiktok_list_video_comments_params,
    tiktok_get_video_transcript_params,
)
from ..._base_client import make_request_options
from ...types.raw.tiktok_get_video_response import TiktokGetVideoResponse
from ...types.raw.tiktok_get_profile_response import TiktokGetProfileResponse
from ...types.raw.tiktok_list_profile_videos_response import TiktokListProfileVideosResponse
from ...types.raw.tiktok_list_video_comments_response import TiktokListVideoCommentsResponse
from ...types.raw.tiktok_get_video_transcript_response import TiktokGetVideoTranscriptResponse

__all__ = ["TiktokResource", "AsyncTiktokResource"]


class TiktokResource(SyncAPIResource):
    """Fetch fresh data directly from social platforms in real-time.

    Use when you need the most current information or data for profiles not yet in our database.
    """

    @cached_property
    def with_raw_response(self) -> TiktokResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TiktokResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TiktokResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return TiktokResourceWithStreamingResponse(self)

    def get_profile(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetProfileResponse:
        """
        Fetch a normalized TikTok profile with current identity, biography,
        verification, and audience metrics.

        **Pricing**: 0.5 credits per profile scraped ($0.005)

        Args:
          username: TikTok username, with or without a leading @

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/v1/raw/tiktok/profile/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TiktokGetProfileResponse,
        )

    def get_video(
        self,
        *,
        url: str,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoResponse:
        """
        Fetch normalized details and current engagement metrics for a TikTok video URL.
        Signed media URLs are temporary and should be downloaded promptly.

        **Pricing**: 0.5 credits per video scraped ($0.005)

        Args:
          url: HTTPS TikTok video or share URL

          region: Two-letter region code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/video",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "region": region,
                    },
                    tiktok_get_video_params.TiktokGetVideoParams,
                ),
            ),
            cast_to=TiktokGetVideoResponse,
        )

    def get_video_transcript(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoTranscriptResponse:
        """
        Fetch or generate a normalized TikTok transcript with plain text and timestamped
        segments. The detected-language transcript is reused on later requests.

        **Pricing**: 5 credits per transcript ($0.05)

        Args:
          url: HTTPS TikTok video or share URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/video/transcript",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, tiktok_get_video_transcript_params.TiktokGetVideoTranscriptParams),
            ),
            cast_to=TiktokGetVideoTranscriptResponse,
        )

    def list_profile_videos(
        self,
        username: str,
        *,
        cursor: str | Omit = omit,
        region: str | Omit = omit,
        sort_by: Literal["latest", "popular"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListProfileVideosResponse:
        """Fetch one cursor-paginated page of normalized TikTok videos.

        Signed media URLs
        are temporary and should be downloaded promptly.

        **Pricing**: 0.5 credits per video page scraped ($0.005)

        Args:
          username: TikTok username, with or without a leading @

          cursor: Opaque cursor from the previous response

          region: Two-letter region code

          sort_by: Video ordering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/v1/raw/tiktok/profile/{username}/videos", username=username),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "region": region,
                        "sort_by": sort_by,
                    },
                    tiktok_list_profile_videos_params.TiktokListProfileVideosParams,
                ),
            ),
            cast_to=TiktokListProfileVideosResponse,
        )

    def list_video_comments(
        self,
        *,
        url: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListVideoCommentsResponse:
        """
        Fetch one cursor-paginated page of normalized comments for a TikTok video URL.

        **Pricing**: 0.5 credits per comment page scraped ($0.005)

        Args:
          url: HTTPS TikTok video or share URL

          cursor: Opaque cursor from the previous response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/video/comments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "cursor": cursor,
                    },
                    tiktok_list_video_comments_params.TiktokListVideoCommentsParams,
                ),
            ),
            cast_to=TiktokListVideoCommentsResponse,
        )


class AsyncTiktokResource(AsyncAPIResource):
    """Fetch fresh data directly from social platforms in real-time.

    Use when you need the most current information or data for profiles not yet in our database.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTiktokResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTiktokResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTiktokResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncTiktokResourceWithStreamingResponse(self)

    async def get_profile(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetProfileResponse:
        """
        Fetch a normalized TikTok profile with current identity, biography,
        verification, and audience metrics.

        **Pricing**: 0.5 credits per profile scraped ($0.005)

        Args:
          username: TikTok username, with or without a leading @

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/v1/raw/tiktok/profile/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TiktokGetProfileResponse,
        )

    async def get_video(
        self,
        *,
        url: str,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoResponse:
        """
        Fetch normalized details and current engagement metrics for a TikTok video URL.
        Signed media URLs are temporary and should be downloaded promptly.

        **Pricing**: 0.5 credits per video scraped ($0.005)

        Args:
          url: HTTPS TikTok video or share URL

          region: Two-letter region code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/video",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "region": region,
                    },
                    tiktok_get_video_params.TiktokGetVideoParams,
                ),
            ),
            cast_to=TiktokGetVideoResponse,
        )

    async def get_video_transcript(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoTranscriptResponse:
        """
        Fetch or generate a normalized TikTok transcript with plain text and timestamped
        segments. The detected-language transcript is reused on later requests.

        **Pricing**: 5 credits per transcript ($0.05)

        Args:
          url: HTTPS TikTok video or share URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/video/transcript",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url": url}, tiktok_get_video_transcript_params.TiktokGetVideoTranscriptParams
                ),
            ),
            cast_to=TiktokGetVideoTranscriptResponse,
        )

    async def list_profile_videos(
        self,
        username: str,
        *,
        cursor: str | Omit = omit,
        region: str | Omit = omit,
        sort_by: Literal["latest", "popular"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListProfileVideosResponse:
        """Fetch one cursor-paginated page of normalized TikTok videos.

        Signed media URLs
        are temporary and should be downloaded promptly.

        **Pricing**: 0.5 credits per video page scraped ($0.005)

        Args:
          username: TikTok username, with or without a leading @

          cursor: Opaque cursor from the previous response

          region: Two-letter region code

          sort_by: Video ordering

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/v1/raw/tiktok/profile/{username}/videos", username=username),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "region": region,
                        "sort_by": sort_by,
                    },
                    tiktok_list_profile_videos_params.TiktokListProfileVideosParams,
                ),
            ),
            cast_to=TiktokListProfileVideosResponse,
        )

    async def list_video_comments(
        self,
        *,
        url: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListVideoCommentsResponse:
        """
        Fetch one cursor-paginated page of normalized comments for a TikTok video URL.

        **Pricing**: 0.5 credits per comment page scraped ($0.005)

        Args:
          url: HTTPS TikTok video or share URL

          cursor: Opaque cursor from the previous response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/video/comments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "cursor": cursor,
                    },
                    tiktok_list_video_comments_params.TiktokListVideoCommentsParams,
                ),
            ),
            cast_to=TiktokListVideoCommentsResponse,
        )


class TiktokResourceWithRawResponse:
    def __init__(self, tiktok: TiktokResource) -> None:
        self._tiktok = tiktok

        self.get_profile = to_raw_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = to_raw_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_transcript = to_raw_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.list_profile_videos = to_raw_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = to_raw_response_wrapper(
            tiktok.list_video_comments,
        )


class AsyncTiktokResourceWithRawResponse:
    def __init__(self, tiktok: AsyncTiktokResource) -> None:
        self._tiktok = tiktok

        self.get_profile = async_to_raw_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = async_to_raw_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_transcript = async_to_raw_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.list_profile_videos = async_to_raw_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = async_to_raw_response_wrapper(
            tiktok.list_video_comments,
        )


class TiktokResourceWithStreamingResponse:
    def __init__(self, tiktok: TiktokResource) -> None:
        self._tiktok = tiktok

        self.get_profile = to_streamed_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = to_streamed_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_transcript = to_streamed_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.list_profile_videos = to_streamed_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = to_streamed_response_wrapper(
            tiktok.list_video_comments,
        )


class AsyncTiktokResourceWithStreamingResponse:
    def __init__(self, tiktok: AsyncTiktokResource) -> None:
        self._tiktok = tiktok

        self.get_profile = async_to_streamed_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = async_to_streamed_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_transcript = async_to_streamed_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.list_profile_videos = async_to_streamed_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = async_to_streamed_response_wrapper(
            tiktok.list_video_comments,
        )
