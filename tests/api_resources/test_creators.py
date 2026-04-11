# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types import (
    CreatorMatchResponse,
    CreatorRetrieveResponse,
    CreatorLookalikeResponse,
    CreatorAutocompleteResponse,
)
from influship.pagination import SyncBodyCursor, AsyncBodyCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Influship) -> None:
        creator = client.creators.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            include=["profiles"],
        )
        assert_matches_type(CreatorRetrieveResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Influship) -> None:
        response = client.creators.with_raw_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            include=["profiles"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = response.parse()
        assert_matches_type(CreatorRetrieveResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Influship) -> None:
        with client.creators.with_streaming_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            include=["profiles"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = response.parse()
            assert_matches_type(CreatorRetrieveResponse, creator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.creators.with_raw_response.retrieve(
                id="",
                include=["profiles"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete(self, client: Influship) -> None:
        creator = client.creators.autocomplete(
            q="fitness",
        )
        assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_with_all_params(self, client: Influship) -> None:
        creator = client.creators.autocomplete(
            q="fitness",
            limit=5,
            platform="instagram",
            scope="all_platforms",
        )
        assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete(self, client: Influship) -> None:
        response = client.creators.with_raw_response.autocomplete(
            q="fitness",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = response.parse()
        assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete(self, client: Influship) -> None:
        with client.creators.with_streaming_response.autocomplete(
            q="fitness",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = response.parse()
            assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookalike(self, client: Influship) -> None:
        creator = client.creators.lookalike(
            seeds=[{}],
        )
        assert_matches_type(SyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookalike_with_all_params(self, client: Influship) -> None:
        creator = client.creators.lookalike(
            seeds=[
                {
                    "creator_id": "123e4567-e89b-12d3-a456-426614174000",
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                    "weight": 1,
                }
            ],
            cursor="cursor",
            filters={
                "engagement_rate": {
                    "max": 10,
                    "min": 1.5,
                },
                "followers": {
                    "max": 500000,
                    "min": 25000,
                },
                "verified": True,
            },
            limit=20,
        )
        assert_matches_type(SyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookalike(self, client: Influship) -> None:
        response = client.creators.with_raw_response.lookalike(
            seeds=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = response.parse()
        assert_matches_type(SyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookalike(self, client: Influship) -> None:
        with client.creators.with_streaming_response.lookalike(
            seeds=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = response.parse()
            assert_matches_type(SyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_match(self, client: Influship) -> None:
        creator = client.creators.match(
            creators=[{}, {}],
            intent={"query": "Promote our new plant-based protein powder"},
        )
        assert_matches_type(CreatorMatchResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_match_with_all_params(self, client: Influship) -> None:
        creator = client.creators.match(
            creators=[
                {
                    "creator_id": "123e4567-e89b-12d3-a456-426614174000",
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                },
                {
                    "creator_id": "123e4567-e89b-12d3-a456-426614174000",
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                },
            ],
            intent={
                "query": "Promote our new plant-based protein powder",
                "context": "Target audience is health-conscious millennials interested in sustainable fitness",
            },
        )
        assert_matches_type(CreatorMatchResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_match(self, client: Influship) -> None:
        response = client.creators.with_raw_response.match(
            creators=[{}, {}],
            intent={"query": "Promote our new plant-based protein powder"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = response.parse()
        assert_matches_type(CreatorMatchResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_match(self, client: Influship) -> None:
        with client.creators.with_streaming_response.match(
            creators=[{}, {}],
            intent={"query": "Promote our new plant-based protein powder"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = response.parse()
            assert_matches_type(CreatorMatchResponse, creator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            include=["profiles"],
        )
        assert_matches_type(CreatorRetrieveResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInfluship) -> None:
        response = await async_client.creators.with_raw_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            include=["profiles"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = await response.parse()
        assert_matches_type(CreatorRetrieveResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInfluship) -> None:
        async with async_client.creators.with_streaming_response.retrieve(
            id="123e4567-e89b-12d3-a456-426614174000",
            include=["profiles"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = await response.parse()
            assert_matches_type(CreatorRetrieveResponse, creator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.creators.with_raw_response.retrieve(
                id="",
                include=["profiles"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.autocomplete(
            q="fitness",
        )
        assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_with_all_params(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.autocomplete(
            q="fitness",
            limit=5,
            platform="instagram",
            scope="all_platforms",
        )
        assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete(self, async_client: AsyncInfluship) -> None:
        response = await async_client.creators.with_raw_response.autocomplete(
            q="fitness",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = await response.parse()
        assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete(self, async_client: AsyncInfluship) -> None:
        async with async_client.creators.with_streaming_response.autocomplete(
            q="fitness",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = await response.parse()
            assert_matches_type(CreatorAutocompleteResponse, creator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookalike(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.lookalike(
            seeds=[{}],
        )
        assert_matches_type(AsyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookalike_with_all_params(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.lookalike(
            seeds=[
                {
                    "creator_id": "123e4567-e89b-12d3-a456-426614174000",
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                    "weight": 1,
                }
            ],
            cursor="cursor",
            filters={
                "engagement_rate": {
                    "max": 10,
                    "min": 1.5,
                },
                "followers": {
                    "max": 500000,
                    "min": 25000,
                },
                "verified": True,
            },
            limit=20,
        )
        assert_matches_type(AsyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookalike(self, async_client: AsyncInfluship) -> None:
        response = await async_client.creators.with_raw_response.lookalike(
            seeds=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = await response.parse()
        assert_matches_type(AsyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookalike(self, async_client: AsyncInfluship) -> None:
        async with async_client.creators.with_streaming_response.lookalike(
            seeds=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = await response.parse()
            assert_matches_type(AsyncBodyCursor[CreatorLookalikeResponse], creator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_match(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.match(
            creators=[{}, {}],
            intent={"query": "Promote our new plant-based protein powder"},
        )
        assert_matches_type(CreatorMatchResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_match_with_all_params(self, async_client: AsyncInfluship) -> None:
        creator = await async_client.creators.match(
            creators=[
                {
                    "creator_id": "123e4567-e89b-12d3-a456-426614174000",
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                },
                {
                    "creator_id": "123e4567-e89b-12d3-a456-426614174000",
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                },
            ],
            intent={
                "query": "Promote our new plant-based protein powder",
                "context": "Target audience is health-conscious millennials interested in sustainable fitness",
            },
        )
        assert_matches_type(CreatorMatchResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_match(self, async_client: AsyncInfluship) -> None:
        response = await async_client.creators.with_raw_response.match(
            creators=[{}, {}],
            intent={"query": "Promote our new plant-based protein powder"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator = await response.parse()
        assert_matches_type(CreatorMatchResponse, creator, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_match(self, async_client: AsyncInfluship) -> None:
        async with async_client.creators.with_streaming_response.match(
            creators=[{}, {}],
            intent={"query": "Promote our new plant-based protein powder"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator = await response.parse()
            assert_matches_type(CreatorMatchResponse, creator, path=["response"])

        assert cast(Any, response.is_closed) is True
