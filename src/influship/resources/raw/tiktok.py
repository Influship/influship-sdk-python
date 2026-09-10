# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
    tiktok_get_music_params,
    tiktok_get_video_params,
    tiktok_get_videos_params,
    tiktok_search_users_params,
    tiktok_search_videos_params,
    tiktok_list_music_videos_params,
    tiktok_get_video_captions_params,
    tiktok_list_hashtag_videos_params,
    tiktok_list_profile_videos_params,
    tiktok_list_video_comments_params,
    tiktok_get_video_transcript_params,
    tiktok_list_comment_replies_params,
    tiktok_get_video_transcripts_params,
)
from ..._base_client import make_request_options
from ...types.raw.tiktok_get_music_response import TiktokGetMusicResponse
from ...types.raw.tiktok_get_video_response import TiktokGetVideoResponse
from ...types.raw.tiktok_get_videos_response import TiktokGetVideosResponse
from ...types.raw.tiktok_get_profile_response import TiktokGetProfileResponse
from ...types.raw.tiktok_search_users_response import TiktokSearchUsersResponse
from ...types.raw.tiktok_search_videos_response import TiktokSearchVideosResponse
from ...types.raw.tiktok_list_music_videos_response import TiktokListMusicVideosResponse
from ...types.raw.tiktok_get_video_captions_response import TiktokGetVideoCaptionsResponse
from ...types.raw.tiktok_list_hashtag_videos_response import TiktokListHashtagVideosResponse
from ...types.raw.tiktok_list_profile_videos_response import TiktokListProfileVideosResponse
from ...types.raw.tiktok_list_video_comments_response import TiktokListVideoCommentsResponse
from ...types.raw.tiktok_get_video_transcript_response import TiktokGetVideoTranscriptResponse
from ...types.raw.tiktok_list_comment_replies_response import TiktokListCommentRepliesResponse
from ...types.raw.tiktok_get_video_transcripts_response import TiktokGetVideoTranscriptsResponse

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

    def get_music(
        self,
        *,
        music_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetMusicResponse:
        """Fetch metadata for a TikTok sound clip by music_id.

        Unknown fields are null.
        Audio and cover URLs are temporary upstream links, not durable downloads.

        **Pricing**: 0.2 credits per sound lookup ($0.002)

        Args:
          music_id: TikTok sound clip ID, not a recording or album ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/music",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"music_id": music_id}, tiktok_get_music_params.TiktokGetMusicParams),
            ),
            cast_to=TiktokGetMusicResponse,
        )

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

        **Pricing**: 0.2 credits per profile scraped ($0.002)

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
        region: Literal["US"] | Omit = omit,
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

        **Pricing**: 0.2 credits per video scraped ($0.002)

        Args:
          url: HTTPS TikTok video or share URL

          region: TikTok resolution region (US only)

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

    def get_video_captions(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoCaptionsResponse:
        """Return available TikTok captions without generating a transcript.

        Returns
        transcript_not_available when captions are unavailable. Successful cached
        results are charged at the ordinary rate.

        **Pricing**: 0.2 credits per successful caption response ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/video/captions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, tiktok_get_video_captions_params.TiktokGetVideoCaptionsParams),
            ),
            cast_to=TiktokGetVideoCaptionsResponse,
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

        **Pricing**: 2.5 credits per transcript ($0.025)

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

    def get_video_transcripts(
        self,
        *,
        urls: SequenceNotStr[str],
        mode: Literal["auto", "captions"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoTranscriptsResponse:
        """Process up to 10 video URLs with ordered per-item results.

        Choose auto (default,
        $0.025 per item) or captions ($0.002 per item, never generates). Account credits
        charge successful items only. Premium payments quote all requested items and are
        nonrefundable once settled, including partial or failed items in a completed
        batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/raw/tiktok/video/transcripts",
            body=maybe_transform(
                {
                    "urls": urls,
                    "mode": mode,
                },
                tiktok_get_video_transcripts_params.TiktokGetVideoTranscriptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TiktokGetVideoTranscriptsResponse,
        )

    def get_videos(
        self,
        *,
        urls: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideosResponse:
        """Fetch up to 20 video URLs with ordered per-item results.

        Duplicate entries
        remain distinct requested items. Account credits charge successful items only at
        $0.002 each. Premium payments quote all requested items and are nonrefundable
        once settled, including partial or failed items in a completed batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/raw/tiktok/videos",
            body=maybe_transform({"urls": urls}, tiktok_get_videos_params.TiktokGetVideosParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TiktokGetVideosResponse,
        )

    def list_comment_replies(
        self,
        *,
        comment_id: str,
        url: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListCommentRepliesResponse:
        """Fetch one cursor-paginated page of replies to a numeric parent comment ID.

        Keep
        the same video URL and parent comment ID when continuing with next_cursor.

        **Pricing**: 0.2 credits per reply page scraped ($0.002)

        Args:
          comment_id: Numeric ID of the parent comment

          url: HTTPS TikTok video or share URL

          cursor: Opaque cursor from the previous response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/video/comment/replies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "comment_id": comment_id,
                        "url": url,
                        "cursor": cursor,
                    },
                    tiktok_list_comment_replies_params.TiktokListCommentRepliesParams,
                ),
            ),
            cast_to=TiktokListCommentRepliesResponse,
        )

    def list_hashtag_videos(
        self,
        *,
        hashtag: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListHashtagVideosResponse:
        """Fetch one page of videos under a hashtag, supplied without #.

        Continue with
        next_cursor and the same hashtag; cursors are opaque. Duplicate results are
        preserved. Each successful page, including an empty page, is charged once. Media
        links are temporary.

        **Pricing**: 0.2 credits per hashtag video page ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/hashtag/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hashtag": hashtag,
                        "cursor": cursor,
                    },
                    tiktok_list_hashtag_videos_params.TiktokListHashtagVideosParams,
                ),
            ),
            cast_to=TiktokListHashtagVideosResponse,
        )

    def list_music_videos(
        self,
        *,
        music_id: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListMusicVideosResponse:
        """
        Fetch one page of TikTok videos using a sound clip, identified by music_id.
        Continue with next_cursor and the same music_id; cursors are opaque. Duplicate
        results are preserved. Each successful page, including an empty page, is charged
        once. Media links are temporary.

        **Pricing**: 0.2 credits per music video page ($0.002)

        Args:
          music_id: TikTok sound clip ID, not a recording or album ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/music/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "music_id": music_id,
                        "cursor": cursor,
                    },
                    tiktok_list_music_videos_params.TiktokListMusicVideosParams,
                ),
            ),
            cast_to=TiktokListMusicVideosResponse,
        )

    def list_profile_videos(
        self,
        username: str,
        *,
        cursor: str | Omit = omit,
        region: Literal["US"] | Omit = omit,
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

        **Pricing**: 0.2 credits per video page scraped ($0.002)

        Args:
          username: TikTok username, with or without a leading @

          cursor: Opaque cursor from the previous response

          region: TikTok resolution region (US only)

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

        **Pricing**: 0.2 credits per comment page scraped ($0.002)

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

    def search_users(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokSearchUsersResponse:
        """Fetch one page of TikTok user search results.

        Unknown profile fields are null.
        Continue with next_cursor and the same query; treat cursors as opaque. A
        successful page is charged once, including an empty page.

        **Pricing**: 0.2 credits per user search page ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/search/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "cursor": cursor,
                    },
                    tiktok_search_users_params.TiktokSearchUsersParams,
                ),
            ),
            cast_to=TiktokSearchUsersResponse,
        )

    def search_videos(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokSearchVideosResponse:
        """Fetch one relevance-ordered page of TikTok videos matching a query.

        Continue
        with next_cursor and the same query; cursors are opaque. Duplicate results are
        preserved. Each successful page, including an empty page, is charged once. Media
        links are temporary.

        **Pricing**: 0.2 credits per video search page ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/raw/tiktok/search/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "cursor": cursor,
                    },
                    tiktok_search_videos_params.TiktokSearchVideosParams,
                ),
            ),
            cast_to=TiktokSearchVideosResponse,
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

    async def get_music(
        self,
        *,
        music_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetMusicResponse:
        """Fetch metadata for a TikTok sound clip by music_id.

        Unknown fields are null.
        Audio and cover URLs are temporary upstream links, not durable downloads.

        **Pricing**: 0.2 credits per sound lookup ($0.002)

        Args:
          music_id: TikTok sound clip ID, not a recording or album ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/music",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"music_id": music_id}, tiktok_get_music_params.TiktokGetMusicParams),
            ),
            cast_to=TiktokGetMusicResponse,
        )

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

        **Pricing**: 0.2 credits per profile scraped ($0.002)

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
        region: Literal["US"] | Omit = omit,
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

        **Pricing**: 0.2 credits per video scraped ($0.002)

        Args:
          url: HTTPS TikTok video or share URL

          region: TikTok resolution region (US only)

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

    async def get_video_captions(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoCaptionsResponse:
        """Return available TikTok captions without generating a transcript.

        Returns
        transcript_not_available when captions are unavailable. Successful cached
        results are charged at the ordinary rate.

        **Pricing**: 0.2 credits per successful caption response ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/video/captions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url": url}, tiktok_get_video_captions_params.TiktokGetVideoCaptionsParams
                ),
            ),
            cast_to=TiktokGetVideoCaptionsResponse,
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

        **Pricing**: 2.5 credits per transcript ($0.025)

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

    async def get_video_transcripts(
        self,
        *,
        urls: SequenceNotStr[str],
        mode: Literal["auto", "captions"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideoTranscriptsResponse:
        """Process up to 10 video URLs with ordered per-item results.

        Choose auto (default,
        $0.025 per item) or captions ($0.002 per item, never generates). Account credits
        charge successful items only. Premium payments quote all requested items and are
        nonrefundable once settled, including partial or failed items in a completed
        batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/raw/tiktok/video/transcripts",
            body=await async_maybe_transform(
                {
                    "urls": urls,
                    "mode": mode,
                },
                tiktok_get_video_transcripts_params.TiktokGetVideoTranscriptsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TiktokGetVideoTranscriptsResponse,
        )

    async def get_videos(
        self,
        *,
        urls: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokGetVideosResponse:
        """Fetch up to 20 video URLs with ordered per-item results.

        Duplicate entries
        remain distinct requested items. Account credits charge successful items only at
        $0.002 each. Premium payments quote all requested items and are nonrefundable
        once settled, including partial or failed items in a completed batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/raw/tiktok/videos",
            body=await async_maybe_transform({"urls": urls}, tiktok_get_videos_params.TiktokGetVideosParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TiktokGetVideosResponse,
        )

    async def list_comment_replies(
        self,
        *,
        comment_id: str,
        url: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListCommentRepliesResponse:
        """Fetch one cursor-paginated page of replies to a numeric parent comment ID.

        Keep
        the same video URL and parent comment ID when continuing with next_cursor.

        **Pricing**: 0.2 credits per reply page scraped ($0.002)

        Args:
          comment_id: Numeric ID of the parent comment

          url: HTTPS TikTok video or share URL

          cursor: Opaque cursor from the previous response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/video/comment/replies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "comment_id": comment_id,
                        "url": url,
                        "cursor": cursor,
                    },
                    tiktok_list_comment_replies_params.TiktokListCommentRepliesParams,
                ),
            ),
            cast_to=TiktokListCommentRepliesResponse,
        )

    async def list_hashtag_videos(
        self,
        *,
        hashtag: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListHashtagVideosResponse:
        """Fetch one page of videos under a hashtag, supplied without #.

        Continue with
        next_cursor and the same hashtag; cursors are opaque. Duplicate results are
        preserved. Each successful page, including an empty page, is charged once. Media
        links are temporary.

        **Pricing**: 0.2 credits per hashtag video page ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/hashtag/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "hashtag": hashtag,
                        "cursor": cursor,
                    },
                    tiktok_list_hashtag_videos_params.TiktokListHashtagVideosParams,
                ),
            ),
            cast_to=TiktokListHashtagVideosResponse,
        )

    async def list_music_videos(
        self,
        *,
        music_id: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokListMusicVideosResponse:
        """
        Fetch one page of TikTok videos using a sound clip, identified by music_id.
        Continue with next_cursor and the same music_id; cursors are opaque. Duplicate
        results are preserved. Each successful page, including an empty page, is charged
        once. Media links are temporary.

        **Pricing**: 0.2 credits per music video page ($0.002)

        Args:
          music_id: TikTok sound clip ID, not a recording or album ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/music/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "music_id": music_id,
                        "cursor": cursor,
                    },
                    tiktok_list_music_videos_params.TiktokListMusicVideosParams,
                ),
            ),
            cast_to=TiktokListMusicVideosResponse,
        )

    async def list_profile_videos(
        self,
        username: str,
        *,
        cursor: str | Omit = omit,
        region: Literal["US"] | Omit = omit,
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

        **Pricing**: 0.2 credits per video page scraped ($0.002)

        Args:
          username: TikTok username, with or without a leading @

          cursor: Opaque cursor from the previous response

          region: TikTok resolution region (US only)

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

        **Pricing**: 0.2 credits per comment page scraped ($0.002)

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

    async def search_users(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokSearchUsersResponse:
        """Fetch one page of TikTok user search results.

        Unknown profile fields are null.
        Continue with next_cursor and the same query; treat cursors as opaque. A
        successful page is charged once, including an empty page.

        **Pricing**: 0.2 credits per user search page ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/search/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "cursor": cursor,
                    },
                    tiktok_search_users_params.TiktokSearchUsersParams,
                ),
            ),
            cast_to=TiktokSearchUsersResponse,
        )

    async def search_videos(
        self,
        *,
        query: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TiktokSearchVideosResponse:
        """Fetch one relevance-ordered page of TikTok videos matching a query.

        Continue
        with next_cursor and the same query; cursors are opaque. Duplicate results are
        preserved. Each successful page, including an empty page, is charged once. Media
        links are temporary.

        **Pricing**: 0.2 credits per video search page ($0.002)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/raw/tiktok/search/videos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "cursor": cursor,
                    },
                    tiktok_search_videos_params.TiktokSearchVideosParams,
                ),
            ),
            cast_to=TiktokSearchVideosResponse,
        )


class TiktokResourceWithRawResponse:
    def __init__(self, tiktok: TiktokResource) -> None:
        self._tiktok = tiktok

        self.get_music = to_raw_response_wrapper(
            tiktok.get_music,
        )
        self.get_profile = to_raw_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = to_raw_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_captions = to_raw_response_wrapper(
            tiktok.get_video_captions,
        )
        self.get_video_transcript = to_raw_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.get_video_transcripts = to_raw_response_wrapper(
            tiktok.get_video_transcripts,
        )
        self.get_videos = to_raw_response_wrapper(
            tiktok.get_videos,
        )
        self.list_comment_replies = to_raw_response_wrapper(
            tiktok.list_comment_replies,
        )
        self.list_hashtag_videos = to_raw_response_wrapper(
            tiktok.list_hashtag_videos,
        )
        self.list_music_videos = to_raw_response_wrapper(
            tiktok.list_music_videos,
        )
        self.list_profile_videos = to_raw_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = to_raw_response_wrapper(
            tiktok.list_video_comments,
        )
        self.search_users = to_raw_response_wrapper(
            tiktok.search_users,
        )
        self.search_videos = to_raw_response_wrapper(
            tiktok.search_videos,
        )


class AsyncTiktokResourceWithRawResponse:
    def __init__(self, tiktok: AsyncTiktokResource) -> None:
        self._tiktok = tiktok

        self.get_music = async_to_raw_response_wrapper(
            tiktok.get_music,
        )
        self.get_profile = async_to_raw_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = async_to_raw_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_captions = async_to_raw_response_wrapper(
            tiktok.get_video_captions,
        )
        self.get_video_transcript = async_to_raw_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.get_video_transcripts = async_to_raw_response_wrapper(
            tiktok.get_video_transcripts,
        )
        self.get_videos = async_to_raw_response_wrapper(
            tiktok.get_videos,
        )
        self.list_comment_replies = async_to_raw_response_wrapper(
            tiktok.list_comment_replies,
        )
        self.list_hashtag_videos = async_to_raw_response_wrapper(
            tiktok.list_hashtag_videos,
        )
        self.list_music_videos = async_to_raw_response_wrapper(
            tiktok.list_music_videos,
        )
        self.list_profile_videos = async_to_raw_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = async_to_raw_response_wrapper(
            tiktok.list_video_comments,
        )
        self.search_users = async_to_raw_response_wrapper(
            tiktok.search_users,
        )
        self.search_videos = async_to_raw_response_wrapper(
            tiktok.search_videos,
        )


class TiktokResourceWithStreamingResponse:
    def __init__(self, tiktok: TiktokResource) -> None:
        self._tiktok = tiktok

        self.get_music = to_streamed_response_wrapper(
            tiktok.get_music,
        )
        self.get_profile = to_streamed_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = to_streamed_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_captions = to_streamed_response_wrapper(
            tiktok.get_video_captions,
        )
        self.get_video_transcript = to_streamed_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.get_video_transcripts = to_streamed_response_wrapper(
            tiktok.get_video_transcripts,
        )
        self.get_videos = to_streamed_response_wrapper(
            tiktok.get_videos,
        )
        self.list_comment_replies = to_streamed_response_wrapper(
            tiktok.list_comment_replies,
        )
        self.list_hashtag_videos = to_streamed_response_wrapper(
            tiktok.list_hashtag_videos,
        )
        self.list_music_videos = to_streamed_response_wrapper(
            tiktok.list_music_videos,
        )
        self.list_profile_videos = to_streamed_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = to_streamed_response_wrapper(
            tiktok.list_video_comments,
        )
        self.search_users = to_streamed_response_wrapper(
            tiktok.search_users,
        )
        self.search_videos = to_streamed_response_wrapper(
            tiktok.search_videos,
        )


class AsyncTiktokResourceWithStreamingResponse:
    def __init__(self, tiktok: AsyncTiktokResource) -> None:
        self._tiktok = tiktok

        self.get_music = async_to_streamed_response_wrapper(
            tiktok.get_music,
        )
        self.get_profile = async_to_streamed_response_wrapper(
            tiktok.get_profile,
        )
        self.get_video = async_to_streamed_response_wrapper(
            tiktok.get_video,
        )
        self.get_video_captions = async_to_streamed_response_wrapper(
            tiktok.get_video_captions,
        )
        self.get_video_transcript = async_to_streamed_response_wrapper(
            tiktok.get_video_transcript,
        )
        self.get_video_transcripts = async_to_streamed_response_wrapper(
            tiktok.get_video_transcripts,
        )
        self.get_videos = async_to_streamed_response_wrapper(
            tiktok.get_videos,
        )
        self.list_comment_replies = async_to_streamed_response_wrapper(
            tiktok.list_comment_replies,
        )
        self.list_hashtag_videos = async_to_streamed_response_wrapper(
            tiktok.list_hashtag_videos,
        )
        self.list_music_videos = async_to_streamed_response_wrapper(
            tiktok.list_music_videos,
        )
        self.list_profile_videos = async_to_streamed_response_wrapper(
            tiktok.list_profile_videos,
        )
        self.list_video_comments = async_to_streamed_response_wrapper(
            tiktok.list_video_comments,
        )
        self.search_users = async_to_streamed_response_wrapper(
            tiktok.search_users,
        )
        self.search_videos = async_to_streamed_response_wrapper(
            tiktok.search_videos,
        )
