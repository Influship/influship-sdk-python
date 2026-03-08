# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.raw import (
    youtube_search_params,
    youtube_get_channel_params,
    youtube_get_transcript_params,
    youtube_get_channel_transcripts_params,
)
from ..._base_client import make_request_options
from ...types.raw.youtube_search_response import YoutubeSearchResponse
from ...types.raw.youtube_get_channel_response import YoutubeGetChannelResponse
from ...types.raw.youtube_get_transcript_response import YoutubeGetTranscriptResponse
from ...types.raw.youtube_get_channel_transcripts_response import YoutubeGetChannelTranscriptsResponse

__all__ = ["YoutubeResource", "AsyncYoutubeResource"]


class YoutubeResource(SyncAPIResource):
    """Fetch fresh data directly from social platforms in real-time.

    Use when you need the most current information or data for profiles not yet in our database.
    """

    @cached_property
    def with_raw_response(self) -> YoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return YoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return YoutubeResourceWithStreamingResponse(self)

    def get_channel(
        self,
        handle: str,
        *,
        include_videos: bool | Omit = omit,
        video_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetChannelResponse:
        """
        Fetch fresh YouTube channel data including subscriber count, video count, and
        total views.

        **Pricing**: 0.5 credits per channel scraped ($0.005)

        Args:
          handle: YouTube channel handle

          include_videos: Include recent videos in response

          video_limit: Number of videos to include

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._get(
            f"/v1/raw/youtube/channel/{handle}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_videos": include_videos,
                        "video_limit": video_limit,
                    },
                    youtube_get_channel_params.YoutubeGetChannelParams,
                ),
            ),
            cast_to=YoutubeGetChannelResponse,
        )

    def get_channel_transcripts(
        self,
        handle: str,
        *,
        include_segments: bool | Omit = omit,
        language: str | Omit = omit,
        sort_by: Literal["popular", "newest", "oldest"] | Omit = omit,
        video_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetChannelTranscriptsResponse:
        """Fetch transcripts for multiple videos from a YouTube channel.

        Videos can be
        sorted by popularity, newest, or oldest before selection.

        **Features:**

        - Fetches up to 20 video transcripts per request
        - Sort by popular (most views), newest, or oldest
        - Partial success — individual video failures don't block the response
        - Optional timestamped segments for each transcript

        **Pricing**: 0.5 credits per transcript fetched ($0.005)

        Args:
          handle: YouTube channel handle

          include_segments: Include timestamped transcript segments in response

          language: Language code for transcripts

          sort_by: How to sort channel videos before selecting

          video_limit: Number of videos to fetch transcripts for (max 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._get(
            f"/v1/raw/youtube/channel-transcripts/{handle}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_segments": include_segments,
                        "language": language,
                        "sort_by": sort_by,
                        "video_limit": video_limit,
                    },
                    youtube_get_channel_transcripts_params.YoutubeGetChannelTranscriptsParams,
                ),
            ),
            cast_to=YoutubeGetChannelTranscriptsResponse,
        )

    def get_transcript(
        self,
        video_id: str,
        *,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetTranscriptResponse:
        """Fetch YouTube video transcript/captions.

        Returns timestamped segments and full
        text. Useful for content analysis.

        **Supported sources:**

        - Manual captions (highest quality)
        - Auto-generated captions
        - Multiple language tracks

        **Pricing**: 0.5 credits per transcript ($0.005)

        Args:
          video_id: YouTube video ID

          language: Language code or "auto" for automatic detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not video_id:
            raise ValueError(f"Expected a non-empty value for `video_id` but received {video_id!r}")
        return self._get(
            f"/v1/raw/youtube/transcript/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, youtube_get_transcript_params.YoutubeGetTranscriptParams),
            ),
            cast_to=YoutubeGetTranscriptResponse,
        )

    def search(
        self,
        *,
        q: str,
        country_code: str | Omit = omit,
        language_code: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeSearchResponse:
        """
        Search YouTube videos and channels.

        **Pricing**: 0.5 credits per result returned ($0.005)

        Args:
          q: Search query

          country_code: Country code for localized results (ISO 3166-1 alpha-2)

          language_code: Language code for results

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/youtube/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "country_code": country_code,
                        "language_code": language_code,
                        "limit": limit,
                    },
                    youtube_search_params.YoutubeSearchParams,
                ),
            ),
            cast_to=YoutubeSearchResponse,
        )


class AsyncYoutubeResource(AsyncAPIResource):
    """Fetch fresh data directly from social platforms in real-time.

    Use when you need the most current information or data for profiles not yet in our database.
    """

    @cached_property
    def with_raw_response(self) -> AsyncYoutubeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncYoutubeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYoutubeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncYoutubeResourceWithStreamingResponse(self)

    async def get_channel(
        self,
        handle: str,
        *,
        include_videos: bool | Omit = omit,
        video_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetChannelResponse:
        """
        Fetch fresh YouTube channel data including subscriber count, video count, and
        total views.

        **Pricing**: 0.5 credits per channel scraped ($0.005)

        Args:
          handle: YouTube channel handle

          include_videos: Include recent videos in response

          video_limit: Number of videos to include

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._get(
            f"/v1/raw/youtube/channel/{handle}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_videos": include_videos,
                        "video_limit": video_limit,
                    },
                    youtube_get_channel_params.YoutubeGetChannelParams,
                ),
            ),
            cast_to=YoutubeGetChannelResponse,
        )

    async def get_channel_transcripts(
        self,
        handle: str,
        *,
        include_segments: bool | Omit = omit,
        language: str | Omit = omit,
        sort_by: Literal["popular", "newest", "oldest"] | Omit = omit,
        video_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetChannelTranscriptsResponse:
        """Fetch transcripts for multiple videos from a YouTube channel.

        Videos can be
        sorted by popularity, newest, or oldest before selection.

        **Features:**

        - Fetches up to 20 video transcripts per request
        - Sort by popular (most views), newest, or oldest
        - Partial success — individual video failures don't block the response
        - Optional timestamped segments for each transcript

        **Pricing**: 0.5 credits per transcript fetched ($0.005)

        Args:
          handle: YouTube channel handle

          include_segments: Include timestamped transcript segments in response

          language: Language code for transcripts

          sort_by: How to sort channel videos before selecting

          video_limit: Number of videos to fetch transcripts for (max 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._get(
            f"/v1/raw/youtube/channel-transcripts/{handle}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_segments": include_segments,
                        "language": language,
                        "sort_by": sort_by,
                        "video_limit": video_limit,
                    },
                    youtube_get_channel_transcripts_params.YoutubeGetChannelTranscriptsParams,
                ),
            ),
            cast_to=YoutubeGetChannelTranscriptsResponse,
        )

    async def get_transcript(
        self,
        video_id: str,
        *,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeGetTranscriptResponse:
        """Fetch YouTube video transcript/captions.

        Returns timestamped segments and full
        text. Useful for content analysis.

        **Supported sources:**

        - Manual captions (highest quality)
        - Auto-generated captions
        - Multiple language tracks

        **Pricing**: 0.5 credits per transcript ($0.005)

        Args:
          video_id: YouTube video ID

          language: Language code or "auto" for automatic detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not video_id:
            raise ValueError(f"Expected a non-empty value for `video_id` but received {video_id!r}")
        return await self._get(
            f"/v1/raw/youtube/transcript/{video_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, youtube_get_transcript_params.YoutubeGetTranscriptParams
                ),
            ),
            cast_to=YoutubeGetTranscriptResponse,
        )

    async def search(
        self,
        *,
        q: str,
        country_code: str | Omit = omit,
        language_code: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> YoutubeSearchResponse:
        """
        Search YouTube videos and channels.

        **Pricing**: 0.5 credits per result returned ($0.005)

        Args:
          q: Search query

          country_code: Country code for localized results (ISO 3166-1 alpha-2)

          language_code: Language code for results

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/youtube/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "country_code": country_code,
                        "language_code": language_code,
                        "limit": limit,
                    },
                    youtube_search_params.YoutubeSearchParams,
                ),
            ),
            cast_to=YoutubeSearchResponse,
        )


class YoutubeResourceWithRawResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

        self.get_channel = to_raw_response_wrapper(
            youtube.get_channel,
        )
        self.get_channel_transcripts = to_raw_response_wrapper(
            youtube.get_channel_transcripts,
        )
        self.get_transcript = to_raw_response_wrapper(
            youtube.get_transcript,
        )
        self.search = to_raw_response_wrapper(
            youtube.search,
        )


class AsyncYoutubeResourceWithRawResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

        self.get_channel = async_to_raw_response_wrapper(
            youtube.get_channel,
        )
        self.get_channel_transcripts = async_to_raw_response_wrapper(
            youtube.get_channel_transcripts,
        )
        self.get_transcript = async_to_raw_response_wrapper(
            youtube.get_transcript,
        )
        self.search = async_to_raw_response_wrapper(
            youtube.search,
        )


class YoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: YoutubeResource) -> None:
        self._youtube = youtube

        self.get_channel = to_streamed_response_wrapper(
            youtube.get_channel,
        )
        self.get_channel_transcripts = to_streamed_response_wrapper(
            youtube.get_channel_transcripts,
        )
        self.get_transcript = to_streamed_response_wrapper(
            youtube.get_transcript,
        )
        self.search = to_streamed_response_wrapper(
            youtube.search,
        )


class AsyncYoutubeResourceWithStreamingResponse:
    def __init__(self, youtube: AsyncYoutubeResource) -> None:
        self._youtube = youtube

        self.get_channel = async_to_streamed_response_wrapper(
            youtube.get_channel,
        )
        self.get_channel_transcripts = async_to_streamed_response_wrapper(
            youtube.get_channel_transcripts,
        )
        self.get_transcript = async_to_streamed_response_wrapper(
            youtube.get_transcript,
        )
        self.search = async_to_streamed_response_wrapper(
            youtube.search,
        )
