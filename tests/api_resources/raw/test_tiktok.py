# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types.raw import (
    TiktokGetVideoResponse,
    TiktokGetProfileResponse,
    TiktokListProfileVideosResponse,
    TiktokListVideoCommentsResponse,
    TiktokGetVideoTranscriptResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTiktok:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profile(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.get_profile(
            "creator",
        )
        assert_matches_type(TiktokGetProfileResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_profile(self, client: Influship) -> None:
        response = client.raw.tiktok.with_raw_response.get_profile(
            "creator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = response.parse()
        assert_matches_type(TiktokGetProfileResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_profile(self, client: Influship) -> None:
        with client.raw.tiktok.with_streaming_response.get_profile(
            "creator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = response.parse()
            assert_matches_type(TiktokGetProfileResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_profile(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.raw.tiktok.with_raw_response.get_profile(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_video(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )
        assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_video_with_all_params(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
            region="US",
        )
        assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_video(self, client: Influship) -> None:
        response = client.raw.tiktok.with_raw_response.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = response.parse()
        assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_video(self, client: Influship) -> None:
        with client.raw.tiktok.with_streaming_response.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = response.parse()
            assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_video_transcript(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.get_video_transcript(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )
        assert_matches_type(TiktokGetVideoTranscriptResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_video_transcript(self, client: Influship) -> None:
        response = client.raw.tiktok.with_raw_response.get_video_transcript(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = response.parse()
        assert_matches_type(TiktokGetVideoTranscriptResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_video_transcript(self, client: Influship) -> None:
        with client.raw.tiktok.with_streaming_response.get_video_transcript(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = response.parse()
            assert_matches_type(TiktokGetVideoTranscriptResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_profile_videos(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.list_profile_videos(
            username="creator",
        )
        assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_profile_videos_with_all_params(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.list_profile_videos(
            username="creator",
            cursor="x",
            region="US",
            sort_by="latest",
        )
        assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_profile_videos(self, client: Influship) -> None:
        response = client.raw.tiktok.with_raw_response.list_profile_videos(
            username="creator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = response.parse()
        assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_profile_videos(self, client: Influship) -> None:
        with client.raw.tiktok.with_streaming_response.list_profile_videos(
            username="creator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = response.parse()
            assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_profile_videos(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.raw.tiktok.with_raw_response.list_profile_videos(
                username="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_video_comments(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )
        assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_video_comments_with_all_params(self, client: Influship) -> None:
        tiktok = client.raw.tiktok.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
            cursor="x",
        )
        assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_video_comments(self, client: Influship) -> None:
        response = client.raw.tiktok.with_raw_response.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = response.parse()
        assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_video_comments(self, client: Influship) -> None:
        with client.raw.tiktok.with_streaming_response.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = response.parse()
            assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTiktok:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profile(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.get_profile(
            "creator",
        )
        assert_matches_type(TiktokGetProfileResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_profile(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.tiktok.with_raw_response.get_profile(
            "creator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = await response.parse()
        assert_matches_type(TiktokGetProfileResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_profile(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.tiktok.with_streaming_response.get_profile(
            "creator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = await response.parse()
            assert_matches_type(TiktokGetProfileResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_profile(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.raw.tiktok.with_raw_response.get_profile(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_video(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )
        assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_video_with_all_params(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
            region="US",
        )
        assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_video(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.tiktok.with_raw_response.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = await response.parse()
        assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_video(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.tiktok.with_streaming_response.get_video(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = await response.parse()
            assert_matches_type(TiktokGetVideoResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_video_transcript(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.get_video_transcript(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )
        assert_matches_type(TiktokGetVideoTranscriptResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_video_transcript(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.tiktok.with_raw_response.get_video_transcript(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = await response.parse()
        assert_matches_type(TiktokGetVideoTranscriptResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_video_transcript(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.tiktok.with_streaming_response.get_video_transcript(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = await response.parse()
            assert_matches_type(TiktokGetVideoTranscriptResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_profile_videos(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.list_profile_videos(
            username="creator",
        )
        assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_profile_videos_with_all_params(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.list_profile_videos(
            username="creator",
            cursor="x",
            region="US",
            sort_by="latest",
        )
        assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_profile_videos(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.tiktok.with_raw_response.list_profile_videos(
            username="creator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = await response.parse()
        assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_profile_videos(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.tiktok.with_streaming_response.list_profile_videos(
            username="creator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = await response.parse()
            assert_matches_type(TiktokListProfileVideosResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_profile_videos(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.raw.tiktok.with_raw_response.list_profile_videos(
                username="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_video_comments(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )
        assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_video_comments_with_all_params(self, async_client: AsyncInfluship) -> None:
        tiktok = await async_client.raw.tiktok.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
            cursor="x",
        )
        assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_video_comments(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.tiktok.with_raw_response.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tiktok = await response.parse()
        assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_video_comments(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.tiktok.with_streaming_response.list_video_comments(
            url="https://www.tiktok.com/@creator/video/7517114944362499342",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tiktok = await response.parse()
            assert_matches_type(TiktokListVideoCommentsResponse, tiktok, path=["response"])

        assert cast(Any, response.is_closed) is True
