# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .youtube import (
    YoutubeResource,
    AsyncYoutubeResource,
    YoutubeResourceWithRawResponse,
    AsyncYoutubeResourceWithRawResponse,
    YoutubeResourceWithStreamingResponse,
    AsyncYoutubeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .instagram import (
    InstagramResource,
    AsyncInstagramResource,
    InstagramResourceWithRawResponse,
    AsyncInstagramResourceWithRawResponse,
    InstagramResourceWithStreamingResponse,
    AsyncInstagramResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RawResource", "AsyncRawResource"]


class RawResource(SyncAPIResource):
    @cached_property
    def instagram(self) -> InstagramResource:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return InstagramResource(self._client)

    @cached_property
    def youtube(self) -> YoutubeResource:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return YoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> RawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return RawResourceWithStreamingResponse(self)


class AsyncRawResource(AsyncAPIResource):
    @cached_property
    def instagram(self) -> AsyncInstagramResource:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return AsyncInstagramResource(self._client)

    @cached_property
    def youtube(self) -> AsyncYoutubeResource:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return AsyncYoutubeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRawResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Influship/influship-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRawResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRawResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Influship/influship-sdk-python#with_streaming_response
        """
        return AsyncRawResourceWithStreamingResponse(self)


class RawResourceWithRawResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

    @cached_property
    def instagram(self) -> InstagramResourceWithRawResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return InstagramResourceWithRawResponse(self._raw.instagram)

    @cached_property
    def youtube(self) -> YoutubeResourceWithRawResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return YoutubeResourceWithRawResponse(self._raw.youtube)


class AsyncRawResourceWithRawResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

    @cached_property
    def instagram(self) -> AsyncInstagramResourceWithRawResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return AsyncInstagramResourceWithRawResponse(self._raw.instagram)

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithRawResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return AsyncYoutubeResourceWithRawResponse(self._raw.youtube)


class RawResourceWithStreamingResponse:
    def __init__(self, raw: RawResource) -> None:
        self._raw = raw

    @cached_property
    def instagram(self) -> InstagramResourceWithStreamingResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return InstagramResourceWithStreamingResponse(self._raw.instagram)

    @cached_property
    def youtube(self) -> YoutubeResourceWithStreamingResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return YoutubeResourceWithStreamingResponse(self._raw.youtube)


class AsyncRawResourceWithStreamingResponse:
    def __init__(self, raw: AsyncRawResource) -> None:
        self._raw = raw

    @cached_property
    def instagram(self) -> AsyncInstagramResourceWithStreamingResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return AsyncInstagramResourceWithStreamingResponse(self._raw.instagram)

    @cached_property
    def youtube(self) -> AsyncYoutubeResourceWithStreamingResponse:
        """Fetch fresh data directly from social platforms in real-time.

        Use when you need the most current information or data for profiles not yet in our database.
        """
        return AsyncYoutubeResourceWithStreamingResponse(self._raw.youtube)
