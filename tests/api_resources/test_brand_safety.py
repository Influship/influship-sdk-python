# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types import (
    BrandSafetyAnalyzePostsResponse,
    BrandSafetyAnalyzeCreatorsResponse,
    BrandSafetyAnalyzeProfilesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrandSafety:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_analyze_creators(self, client: Influship) -> None:
        brand_safety = client.brand_safety.analyze_creators(
            creators=[{}],
        )
        assert_matches_type(BrandSafetyAnalyzeCreatorsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_analyze_creators(self, client: Influship) -> None:
        response = client.brand_safety.with_raw_response.analyze_creators(
            creators=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_safety = response.parse()
        assert_matches_type(BrandSafetyAnalyzeCreatorsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_analyze_creators(self, client: Influship) -> None:
        with client.brand_safety.with_streaming_response.analyze_creators(
            creators=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_safety = response.parse()
            assert_matches_type(BrandSafetyAnalyzeCreatorsResponse, brand_safety, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_analyze_posts(self, client: Influship) -> None:
        brand_safety = client.brand_safety.analyze_posts(
            posts=[{}],
        )
        assert_matches_type(BrandSafetyAnalyzePostsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_analyze_posts(self, client: Influship) -> None:
        response = client.brand_safety.with_raw_response.analyze_posts(
            posts=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_safety = response.parse()
        assert_matches_type(BrandSafetyAnalyzePostsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_analyze_posts(self, client: Influship) -> None:
        with client.brand_safety.with_streaming_response.analyze_posts(
            posts=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_safety = response.parse()
            assert_matches_type(BrandSafetyAnalyzePostsResponse, brand_safety, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_analyze_profiles(self, client: Influship) -> None:
        brand_safety = client.brand_safety.analyze_profiles(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )
        assert_matches_type(BrandSafetyAnalyzeProfilesResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_analyze_profiles(self, client: Influship) -> None:
        response = client.brand_safety.with_raw_response.analyze_profiles(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_safety = response.parse()
        assert_matches_type(BrandSafetyAnalyzeProfilesResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_analyze_profiles(self, client: Influship) -> None:
        with client.brand_safety.with_streaming_response.analyze_profiles(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_safety = response.parse()
            assert_matches_type(BrandSafetyAnalyzeProfilesResponse, brand_safety, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBrandSafety:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_analyze_creators(self, async_client: AsyncInfluship) -> None:
        brand_safety = await async_client.brand_safety.analyze_creators(
            creators=[{}],
        )
        assert_matches_type(BrandSafetyAnalyzeCreatorsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_analyze_creators(self, async_client: AsyncInfluship) -> None:
        response = await async_client.brand_safety.with_raw_response.analyze_creators(
            creators=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_safety = await response.parse()
        assert_matches_type(BrandSafetyAnalyzeCreatorsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_creators(self, async_client: AsyncInfluship) -> None:
        async with async_client.brand_safety.with_streaming_response.analyze_creators(
            creators=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_safety = await response.parse()
            assert_matches_type(BrandSafetyAnalyzeCreatorsResponse, brand_safety, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_analyze_posts(self, async_client: AsyncInfluship) -> None:
        brand_safety = await async_client.brand_safety.analyze_posts(
            posts=[{}],
        )
        assert_matches_type(BrandSafetyAnalyzePostsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_analyze_posts(self, async_client: AsyncInfluship) -> None:
        response = await async_client.brand_safety.with_raw_response.analyze_posts(
            posts=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_safety = await response.parse()
        assert_matches_type(BrandSafetyAnalyzePostsResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_posts(self, async_client: AsyncInfluship) -> None:
        async with async_client.brand_safety.with_streaming_response.analyze_posts(
            posts=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_safety = await response.parse()
            assert_matches_type(BrandSafetyAnalyzePostsResponse, brand_safety, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_analyze_profiles(self, async_client: AsyncInfluship) -> None:
        brand_safety = await async_client.brand_safety.analyze_profiles(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )
        assert_matches_type(BrandSafetyAnalyzeProfilesResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_analyze_profiles(self, async_client: AsyncInfluship) -> None:
        response = await async_client.brand_safety.with_raw_response.analyze_profiles(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_safety = await response.parse()
        assert_matches_type(BrandSafetyAnalyzeProfilesResponse, brand_safety, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_analyze_profiles(self, async_client: AsyncInfluship) -> None:
        async with async_client.brand_safety.with_streaming_response.analyze_profiles(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_safety = await response.parse()
            assert_matches_type(BrandSafetyAnalyzeProfilesResponse, brand_safety, path=["response"])

        assert cast(Any, response.is_closed) is True
