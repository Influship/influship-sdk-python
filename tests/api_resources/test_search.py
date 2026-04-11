# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types import SearchCreateResponse, SearchRetrieveResponse
from influship.pagination import SyncQueryCursor, AsyncQueryCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Influship) -> None:
        search = client.search.create(
            query="fitness influencers who post workout videos",
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Influship) -> None:
        search = client.search.create(
            query="fitness influencers who post workout videos",
            filters={
                "engagement_rate": {
                    "max": 10,
                    "min": 2,
                },
                "followers": {
                    "max": 500000,
                    "min": 50000,
                },
                "verified": True,
            },
            limit=10,
            platforms=["instagram"],
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Influship) -> None:
        response = client.search.with_raw_response.create(
            query="fitness influencers who post workout videos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Influship) -> None:
        with client.search.with_streaming_response.create(
            query="fitness influencers who post workout videos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchCreateResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Influship) -> None:
        search = client.search.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(SyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Influship) -> None:
        search = client.search.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            cursor="cursor",
            limit=25,
        )
        assert_matches_type(SyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Influship) -> None:
        response = client.search.with_raw_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Influship) -> None:
        with client.search.with_streaming_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.search.with_raw_response.retrieve(
                id="",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInfluship) -> None:
        search = await async_client.search.create(
            query="fitness influencers who post workout videos",
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInfluship) -> None:
        search = await async_client.search.create(
            query="fitness influencers who post workout videos",
            filters={
                "engagement_rate": {
                    "max": 10,
                    "min": 2,
                },
                "followers": {
                    "max": 500000,
                    "min": 50000,
                },
                "verified": True,
            },
            limit=10,
            platforms=["instagram"],
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInfluship) -> None:
        response = await async_client.search.with_raw_response.create(
            query="fitness influencers who post workout videos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInfluship) -> None:
        async with async_client.search.with_streaming_response.create(
            query="fitness influencers who post workout videos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchCreateResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInfluship) -> None:
        search = await async_client.search.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(AsyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncInfluship) -> None:
        search = await async_client.search.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            cursor="cursor",
            limit=25,
        )
        assert_matches_type(AsyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInfluship) -> None:
        response = await async_client.search.with_raw_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(AsyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInfluship) -> None:
        async with async_client.search.with_streaming_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(AsyncQueryCursor[SearchRetrieveResponse], search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.search.with_raw_response.retrieve(
                id="",
            )
