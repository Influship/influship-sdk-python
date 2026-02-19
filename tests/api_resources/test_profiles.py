# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types import ProfileGetResponse, ProfileLookupResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Influship) -> None:
        profile = client.profiles.get(
            username="fitness_coach_jane",
            platform="instagram",
        )
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Influship) -> None:
        response = client.profiles.with_raw_response.get(
            username="fitness_coach_jane",
            platform="instagram",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Influship) -> None:
        with client.profiles.with_streaming_response.get(
            username="fitness_coach_jane",
            platform="instagram",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileGetResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `platform` but received ''"):
            client.profiles.with_raw_response.get(
                username="fitness_coach_jane",
                platform="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.profiles.with_raw_response.get(
                username="",
                platform="instagram",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: Influship) -> None:
        profile = client.profiles.lookup(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )
        assert_matches_type(ProfileLookupResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: Influship) -> None:
        response = client.profiles.with_raw_response.lookup(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileLookupResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: Influship) -> None:
        with client.profiles.with_streaming_response.lookup(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileLookupResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncInfluship) -> None:
        profile = await async_client.profiles.get(
            username="fitness_coach_jane",
            platform="instagram",
        )
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncInfluship) -> None:
        response = await async_client.profiles.with_raw_response.get(
            username="fitness_coach_jane",
            platform="instagram",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileGetResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncInfluship) -> None:
        async with async_client.profiles.with_streaming_response.get(
            username="fitness_coach_jane",
            platform="instagram",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileGetResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `platform` but received ''"):
            await async_client.profiles.with_raw_response.get(
                username="fitness_coach_jane",
                platform="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.profiles.with_raw_response.get(
                username="",
                platform="instagram",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncInfluship) -> None:
        profile = await async_client.profiles.lookup(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )
        assert_matches_type(ProfileLookupResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncInfluship) -> None:
        response = await async_client.profiles.with_raw_response.lookup(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileLookupResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncInfluship) -> None:
        async with async_client.profiles.with_streaming_response.lookup(
            profiles=[
                {
                    "platform": "instagram",
                    "username": "fitness_coach_jane",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileLookupResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
