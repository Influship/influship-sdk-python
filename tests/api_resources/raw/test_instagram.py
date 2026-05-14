# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types.raw import (
    InstagramGetPostResponse,
    InstagramGetPostsResponse,
    InstagramGetProfileResponse,
    InstagramGetTranscriptResponse,
    InstagramGetTranscriptsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstagram:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_post(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_post(
            "C0ABC123xyz",
        )
        assert_matches_type(InstagramGetPostResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_post(self, client: Influship) -> None:
        response = client.raw.instagram.with_raw_response.get_post(
            "C0ABC123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = response.parse()
        assert_matches_type(InstagramGetPostResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_post(self, client: Influship) -> None:
        with client.raw.instagram.with_streaming_response.get_post(
            "C0ABC123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = response.parse()
            assert_matches_type(InstagramGetPostResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_post(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `shortcode` but received ''"):
            client.raw.instagram.with_raw_response.get_post(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_posts(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_posts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )
        assert_matches_type(InstagramGetPostsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_posts(self, client: Influship) -> None:
        response = client.raw.instagram.with_raw_response.get_posts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = response.parse()
        assert_matches_type(InstagramGetPostsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_posts(self, client: Influship) -> None:
        with client.raw.instagram.with_streaming_response.get_posts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = response.parse()
            assert_matches_type(InstagramGetPostsResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profile(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_profile(
            username="fitness_coach_jane",
        )
        assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profile_with_all_params(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_profile(
            username="fitness_coach_jane",
            include_posts=True,
            post_limit=12,
        )
        assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_profile(self, client: Influship) -> None:
        response = client.raw.instagram.with_raw_response.get_profile(
            username="fitness_coach_jane",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = response.parse()
        assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_profile(self, client: Influship) -> None:
        with client.raw.instagram.with_streaming_response.get_profile(
            username="fitness_coach_jane",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = response.parse()
            assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_profile(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.raw.instagram.with_raw_response.get_profile(
                username="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcript(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_transcript(
            shortcode="C0ABC123xyz",
        )
        assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcript_with_all_params(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_transcript(
            shortcode="C0ABC123xyz",
            language="en",
        )
        assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_transcript(self, client: Influship) -> None:
        response = client.raw.instagram.with_raw_response.get_transcript(
            shortcode="C0ABC123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = response.parse()
        assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_transcript(self, client: Influship) -> None:
        with client.raw.instagram.with_streaming_response.get_transcript(
            shortcode="C0ABC123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = response.parse()
            assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_transcript(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `shortcode` but received ''"):
            client.raw.instagram.with_raw_response.get_transcript(
                shortcode="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcripts(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )
        assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcripts_with_all_params(self, client: Influship) -> None:
        instagram = client.raw.instagram.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
            language="en",
        )
        assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_transcripts(self, client: Influship) -> None:
        response = client.raw.instagram.with_raw_response.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = response.parse()
        assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_transcripts(self, client: Influship) -> None:
        with client.raw.instagram.with_streaming_response.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = response.parse()
            assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstagram:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_post(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_post(
            "C0ABC123xyz",
        )
        assert_matches_type(InstagramGetPostResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_post(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.instagram.with_raw_response.get_post(
            "C0ABC123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = await response.parse()
        assert_matches_type(InstagramGetPostResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_post(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.instagram.with_streaming_response.get_post(
            "C0ABC123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = await response.parse()
            assert_matches_type(InstagramGetPostResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_post(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `shortcode` but received ''"):
            await async_client.raw.instagram.with_raw_response.get_post(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_posts(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_posts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )
        assert_matches_type(InstagramGetPostsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_posts(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.instagram.with_raw_response.get_posts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = await response.parse()
        assert_matches_type(InstagramGetPostsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_posts(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.instagram.with_streaming_response.get_posts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = await response.parse()
            assert_matches_type(InstagramGetPostsResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profile(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_profile(
            username="fitness_coach_jane",
        )
        assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profile_with_all_params(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_profile(
            username="fitness_coach_jane",
            include_posts=True,
            post_limit=12,
        )
        assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_profile(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.instagram.with_raw_response.get_profile(
            username="fitness_coach_jane",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = await response.parse()
        assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_profile(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.instagram.with_streaming_response.get_profile(
            username="fitness_coach_jane",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = await response.parse()
            assert_matches_type(InstagramGetProfileResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_profile(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.raw.instagram.with_raw_response.get_profile(
                username="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcript(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_transcript(
            shortcode="C0ABC123xyz",
        )
        assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcript_with_all_params(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_transcript(
            shortcode="C0ABC123xyz",
            language="en",
        )
        assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_transcript(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.instagram.with_raw_response.get_transcript(
            shortcode="C0ABC123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = await response.parse()
        assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_transcript(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.instagram.with_streaming_response.get_transcript(
            shortcode="C0ABC123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = await response.parse()
            assert_matches_type(InstagramGetTranscriptResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_transcript(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `shortcode` but received ''"):
            await async_client.raw.instagram.with_raw_response.get_transcript(
                shortcode="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcripts(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )
        assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcripts_with_all_params(self, async_client: AsyncInfluship) -> None:
        instagram = await async_client.raw.instagram.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
            language="en",
        )
        assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_transcripts(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.instagram.with_raw_response.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instagram = await response.parse()
        assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_transcripts(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.instagram.with_streaming_response.get_transcripts(
            shortcodes=["C0ABC123xyz", "D1DEF456uvw"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instagram = await response.parse()
            assert_matches_type(InstagramGetTranscriptsResponse, instagram, path=["response"])

        assert cast(Any, response.is_closed) is True
