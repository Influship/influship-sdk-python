# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, InflushipError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import raw, posts, health, search, creators, profiles
    from .resources.posts import PostsResource, AsyncPostsResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.raw.raw import RawResource, AsyncRawResource
    from .resources.creators import CreatorsResource, AsyncCreatorsResource
    from .resources.profiles import ProfilesResource, AsyncProfilesResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Influship",
    "AsyncInfluship",
    "Client",
    "AsyncClient",
]


class Influship(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Influship client instance.

        This automatically infers the `api_key` argument from the `INFLUSHIP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("INFLUSHIP_API_KEY")
        if api_key is None:
            raise InflushipError(
                "The api_key client option must be set either by passing api_key to the client or by setting the INFLUSHIP_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("INFLUSHIP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.influship.com"

        custom_headers_env = os.environ.get("INFLUSHIP_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        """API health and status endpoints"""
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def creators(self) -> CreatorsResource:
        """
        Retrieve creator profiles and discover new creators through search, autocomplete, and lookalike matching. Creators are cross-platform entities that may have profiles on multiple social networks.
        """
        from .resources.creators import CreatorsResource

        return CreatorsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        """AI-powered semantic search to find creators using natural language queries.

        Understands intent and context to match creators based on content themes, audience, and style.
        """
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        """
        Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
        """
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def posts(self) -> PostsResource:
        """
        Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
        """
        from .resources.posts import PostsResource

        return PostsResource(self)

    @cached_property
    def raw(self) -> RawResource:
        from .resources.raw import RawResource

        return RawResource(self)

    @cached_property
    def with_raw_response(self) -> InflushipWithRawResponse:
        return InflushipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InflushipWithStreamedResponse:
        return InflushipWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncInfluship(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncInfluship client instance.

        This automatically infers the `api_key` argument from the `INFLUSHIP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("INFLUSHIP_API_KEY")
        if api_key is None:
            raise InflushipError(
                "The api_key client option must be set either by passing api_key to the client or by setting the INFLUSHIP_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("INFLUSHIP_BASE_URL")
        if base_url is None:
            base_url = f"https://api.influship.com"

        custom_headers_env = os.environ.get("INFLUSHIP_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        """API health and status endpoints"""
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def creators(self) -> AsyncCreatorsResource:
        """
        Retrieve creator profiles and discover new creators through search, autocomplete, and lookalike matching. Creators are cross-platform entities that may have profiles on multiple social networks.
        """
        from .resources.creators import AsyncCreatorsResource

        return AsyncCreatorsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """AI-powered semantic search to find creators using natural language queries.

        Understands intent and context to match creators based on content themes, audience, and style.
        """
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """
        Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
        """
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        """
        Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
        """
        from .resources.posts import AsyncPostsResource

        return AsyncPostsResource(self)

    @cached_property
    def raw(self) -> AsyncRawResource:
        from .resources.raw import AsyncRawResource

        return AsyncRawResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncInflushipWithRawResponse:
        return AsyncInflushipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInflushipWithStreamedResponse:
        return AsyncInflushipWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class InflushipWithRawResponse:
    _client: Influship

    def __init__(self, client: Influship) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        """API health and status endpoints"""
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def creators(self) -> creators.CreatorsResourceWithRawResponse:
        """
        Retrieve creator profiles and discover new creators through search, autocomplete, and lookalike matching. Creators are cross-platform entities that may have profiles on multiple social networks.
        """
        from .resources.creators import CreatorsResourceWithRawResponse

        return CreatorsResourceWithRawResponse(self._client.creators)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        """AI-powered semantic search to find creators using natural language queries.

        Understands intent and context to match creators based on content themes, audience, and style.
        """
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        """
        Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
        """
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def posts(self) -> posts.PostsResourceWithRawResponse:
        """
        Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
        """
        from .resources.posts import PostsResourceWithRawResponse

        return PostsResourceWithRawResponse(self._client.posts)

    @cached_property
    def raw(self) -> raw.RawResourceWithRawResponse:
        from .resources.raw import RawResourceWithRawResponse

        return RawResourceWithRawResponse(self._client.raw)


class AsyncInflushipWithRawResponse:
    _client: AsyncInfluship

    def __init__(self, client: AsyncInfluship) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        """API health and status endpoints"""
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def creators(self) -> creators.AsyncCreatorsResourceWithRawResponse:
        """
        Retrieve creator profiles and discover new creators through search, autocomplete, and lookalike matching. Creators are cross-platform entities that may have profiles on multiple social networks.
        """
        from .resources.creators import AsyncCreatorsResourceWithRawResponse

        return AsyncCreatorsResourceWithRawResponse(self._client.creators)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        """AI-powered semantic search to find creators using natural language queries.

        Understands intent and context to match creators based on content themes, audience, and style.
        """
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        """
        Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
        """
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def posts(self) -> posts.AsyncPostsResourceWithRawResponse:
        """
        Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
        """
        from .resources.posts import AsyncPostsResourceWithRawResponse

        return AsyncPostsResourceWithRawResponse(self._client.posts)

    @cached_property
    def raw(self) -> raw.AsyncRawResourceWithRawResponse:
        from .resources.raw import AsyncRawResourceWithRawResponse

        return AsyncRawResourceWithRawResponse(self._client.raw)


class InflushipWithStreamedResponse:
    _client: Influship

    def __init__(self, client: Influship) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        """API health and status endpoints"""
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def creators(self) -> creators.CreatorsResourceWithStreamingResponse:
        """
        Retrieve creator profiles and discover new creators through search, autocomplete, and lookalike matching. Creators are cross-platform entities that may have profiles on multiple social networks.
        """
        from .resources.creators import CreatorsResourceWithStreamingResponse

        return CreatorsResourceWithStreamingResponse(self._client.creators)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        """AI-powered semantic search to find creators using natural language queries.

        Understands intent and context to match creators based on content themes, audience, and style.
        """
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        """
        Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
        """
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def posts(self) -> posts.PostsResourceWithStreamingResponse:
        """
        Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
        """
        from .resources.posts import PostsResourceWithStreamingResponse

        return PostsResourceWithStreamingResponse(self._client.posts)

    @cached_property
    def raw(self) -> raw.RawResourceWithStreamingResponse:
        from .resources.raw import RawResourceWithStreamingResponse

        return RawResourceWithStreamingResponse(self._client.raw)


class AsyncInflushipWithStreamedResponse:
    _client: AsyncInfluship

    def __init__(self, client: AsyncInfluship) -> None:
        self._client = client

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        """API health and status endpoints"""
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def creators(self) -> creators.AsyncCreatorsResourceWithStreamingResponse:
        """
        Retrieve creator profiles and discover new creators through search, autocomplete, and lookalike matching. Creators are cross-platform entities that may have profiles on multiple social networks.
        """
        from .resources.creators import AsyncCreatorsResourceWithStreamingResponse

        return AsyncCreatorsResourceWithStreamingResponse(self._client.creators)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        """AI-powered semantic search to find creators using natural language queries.

        Understands intent and context to match creators based on content themes, audience, and style.
        """
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        """
        Access individual social media profiles with detailed metrics, growth data, and activity information. Profiles are platform-specific accounts linked to creators.
        """
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def posts(self) -> posts.AsyncPostsResourceWithStreamingResponse:
        """
        Retrieve and analyze social media posts with engagement metrics, media content, and performance data.
        """
        from .resources.posts import AsyncPostsResourceWithStreamingResponse

        return AsyncPostsResourceWithStreamingResponse(self._client.posts)

    @cached_property
    def raw(self) -> raw.AsyncRawResourceWithStreamingResponse:
        from .resources.raw import AsyncRawResourceWithStreamingResponse

        return AsyncRawResourceWithStreamingResponse(self._client.raw)


Client = Influship

AsyncClient = AsyncInfluship
