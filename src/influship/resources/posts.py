# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import post_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncQueryCursor, AsyncQueryCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.post_list_response import PostListResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    """
    Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
    """

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        creator_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        platform: Literal["instagram"] | Omit = omit,
        sort: Literal["recent", "top_engagement", "most_likes", "most_views", "most_comments"] | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncQueryCursor[PostListResponse]:
        """
        Retrieve posts for a creator or profile with engagement metrics and media data.

        **Query options:**

        - By creator: Use `creator_id` to get posts across all their profiles
        - By profile: Use `platform` + `username` for a specific profile's posts

        **Sort options:**

        - `recent`: Most recent posts first (default)
        - `top_engagement`: Highest engagement rate first
        - `most_likes`: Most likes first
        - `most_views`: Most views first (video content)
        - `most_comments`: Most comments first

        **Pricing**: 0.05 credits per post returned ($0.0005)

        Args:
          creator_id: Creator ID (use this OR platform+username)

          cursor: Pagination cursor for next page

          limit: Maximum posts to return

          platform: Platform (required with username)

          sort: Sort order

          username: Username (required with platform)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/posts",
            page=SyncQueryCursor[PostListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "creator_id": creator_id,
                        "cursor": cursor,
                        "limit": limit,
                        "platform": platform,
                        "sort": sort,
                        "username": username,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            model=PostListResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    """
    Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        creator_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        platform: Literal["instagram"] | Omit = omit,
        sort: Literal["recent", "top_engagement", "most_likes", "most_views", "most_comments"] | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PostListResponse, AsyncQueryCursor[PostListResponse]]:
        """
        Retrieve posts for a creator or profile with engagement metrics and media data.

        **Query options:**

        - By creator: Use `creator_id` to get posts across all their profiles
        - By profile: Use `platform` + `username` for a specific profile's posts

        **Sort options:**

        - `recent`: Most recent posts first (default)
        - `top_engagement`: Highest engagement rate first
        - `most_likes`: Most likes first
        - `most_views`: Most views first (video content)
        - `most_comments`: Most comments first

        **Pricing**: 0.05 credits per post returned ($0.0005)

        Args:
          creator_id: Creator ID (use this OR platform+username)

          cursor: Pagination cursor for next page

          limit: Maximum posts to return

          platform: Platform (required with username)

          sort: Sort order

          username: Username (required with platform)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/posts",
            page=AsyncQueryCursor[PostListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "creator_id": creator_id,
                        "cursor": cursor,
                        "limit": limit,
                        "platform": platform,
                        "sort": sort,
                        "username": username,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            model=PostListResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.list = to_raw_response_wrapper(
            posts.list,
        )


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.list = async_to_raw_response_wrapper(
            posts.list,
        )


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.list = to_streamed_response_wrapper(
            posts.list,
        )


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
