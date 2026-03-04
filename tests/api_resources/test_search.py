# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types import SearchCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Influship) -> None:
        search = client.search.create(
            query="fitness influencers with 100k+ followers who post workout videos",
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Influship) -> None:
        search = client.search.create(
            query="fitness influencers with 100k+ followers who post workout videos",
            filters={
                "engagement_rate": {
                    "max": 10,
                    "min": 1.5,
                },
                "followers": {
                    "max": 500000,
                    "min": 10000,
                },
                "verified": True,
            },
            limit=25,
            platforms=["instagram"],
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Influship) -> None:
        response = client.search.with_raw_response.create(
            query="fitness influencers with 100k+ followers who post workout videos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Influship) -> None:
        with client.search.with_streaming_response.create(
            query="fitness influencers with 100k+ followers who post workout videos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchCreateResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInfluship) -> None:
        search = await async_client.search.create(
            query="fitness influencers with 100k+ followers who post workout videos",
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInfluship) -> None:
        search = await async_client.search.create(
            query="fitness influencers with 100k+ followers who post workout videos",
            filters={
                "engagement_rate": {
                    "max": 10,
                    "min": 1.5,
                },
                "followers": {
                    "max": 500000,
                    "min": 10000,
                },
                "verified": True,
            },
            limit=25,
            platforms=["instagram"],
        )
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInfluship) -> None:
        response = await async_client.search.with_raw_response.create(
            query="fitness influencers with 100k+ followers who post workout videos",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchCreateResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInfluship) -> None:
        async with async_client.search.with_streaming_response.create(
            query="fitness influencers with 100k+ followers who post workout videos",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchCreateResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
