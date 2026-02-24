# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types.raw import (
    YoutubeSearchResponse,
    YoutubeGetChannelResponse,
    YoutubeGetTranscriptResponse,
    YoutubeGetChannelTranscriptsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestYoutube:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_channel(self, client: Influship) -> None:
        youtube = client.raw.youtube.get_channel(
            handle="@techreviews",
        )
        assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_channel_with_all_params(self, client: Influship) -> None:
        youtube = client.raw.youtube.get_channel(
            handle="@techreviews",
            include_videos=True,
            video_limit=12,
        )
        assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_channel(self, client: Influship) -> None:
        response = client.raw.youtube.with_raw_response.get_channel(
            handle="@techreviews",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_channel(self, client: Influship) -> None:
        with client.raw.youtube.with_streaming_response.get_channel(
            handle="@techreviews",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_channel(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.raw.youtube.with_raw_response.get_channel(
                handle="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_channel_transcripts(self, client: Influship) -> None:
        youtube = client.raw.youtube.get_channel_transcripts(
            handle="@techreviews",
        )
        assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_channel_transcripts_with_all_params(self, client: Influship) -> None:
        youtube = client.raw.youtube.get_channel_transcripts(
            handle="@techreviews",
            include_segments=False,
            language="en",
            sort_by="newest",
            video_limit=5,
        )
        assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_channel_transcripts(self, client: Influship) -> None:
        response = client.raw.youtube.with_raw_response.get_channel_transcripts(
            handle="@techreviews",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_channel_transcripts(self, client: Influship) -> None:
        with client.raw.youtube.with_streaming_response.get_channel_transcripts(
            handle="@techreviews",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_channel_transcripts(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.raw.youtube.with_raw_response.get_channel_transcripts(
                handle="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcript(self, client: Influship) -> None:
        youtube = client.raw.youtube.get_transcript(
            video_id="dQw4w9WgXcQ",
        )
        assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcript_with_all_params(self, client: Influship) -> None:
        youtube = client.raw.youtube.get_transcript(
            video_id="dQw4w9WgXcQ",
            language="en",
        )
        assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_transcript(self, client: Influship) -> None:
        response = client.raw.youtube.with_raw_response.get_transcript(
            video_id="dQw4w9WgXcQ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_transcript(self, client: Influship) -> None:
        with client.raw.youtube.with_streaming_response.get_transcript(
            video_id="dQw4w9WgXcQ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_transcript(self, client: Influship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `video_id` but received ''"):
            client.raw.youtube.with_raw_response.get_transcript(
                video_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Influship) -> None:
        youtube = client.raw.youtube.search(
            q="fitness workout",
        )
        assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Influship) -> None:
        youtube = client.raw.youtube.search(
            q="fitness workout",
            country_code="US",
            language_code="en",
            limit=20,
        )
        assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Influship) -> None:
        response = client.raw.youtube.with_raw_response.search(
            q="fitness workout",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = response.parse()
        assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Influship) -> None:
        with client.raw.youtube.with_streaming_response.search(
            q="fitness workout",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = response.parse()
            assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncYoutube:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_channel(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.get_channel(
            handle="@techreviews",
        )
        assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_channel_with_all_params(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.get_channel(
            handle="@techreviews",
            include_videos=True,
            video_limit=12,
        )
        assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_channel(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.youtube.with_raw_response.get_channel(
            handle="@techreviews",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_channel(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.youtube.with_streaming_response.get_channel(
            handle="@techreviews",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetChannelResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_channel(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.raw.youtube.with_raw_response.get_channel(
                handle="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_channel_transcripts(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.get_channel_transcripts(
            handle="@techreviews",
        )
        assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_channel_transcripts_with_all_params(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.get_channel_transcripts(
            handle="@techreviews",
            include_segments=False,
            language="en",
            sort_by="newest",
            video_limit=5,
        )
        assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_channel_transcripts(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.youtube.with_raw_response.get_channel_transcripts(
            handle="@techreviews",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_channel_transcripts(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.youtube.with_streaming_response.get_channel_transcripts(
            handle="@techreviews",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetChannelTranscriptsResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_channel_transcripts(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.raw.youtube.with_raw_response.get_channel_transcripts(
                handle="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcript(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.get_transcript(
            video_id="dQw4w9WgXcQ",
        )
        assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcript_with_all_params(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.get_transcript(
            video_id="dQw4w9WgXcQ",
            language="en",
        )
        assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_transcript(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.youtube.with_raw_response.get_transcript(
            video_id="dQw4w9WgXcQ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_transcript(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.youtube.with_streaming_response.get_transcript(
            video_id="dQw4w9WgXcQ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeGetTranscriptResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_transcript(self, async_client: AsyncInfluship) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `video_id` but received ''"):
            await async_client.raw.youtube.with_raw_response.get_transcript(
                video_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.search(
            q="fitness workout",
        )
        assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncInfluship) -> None:
        youtube = await async_client.raw.youtube.search(
            q="fitness workout",
            country_code="US",
            language_code="en",
            limit=20,
        )
        assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncInfluship) -> None:
        response = await async_client.raw.youtube.with_raw_response.search(
            q="fitness workout",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        youtube = await response.parse()
        assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncInfluship) -> None:
        async with async_client.raw.youtube.with_streaming_response.search(
            q="fitness workout",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            youtube = await response.parse()
            assert_matches_type(YoutubeSearchResponse, youtube, path=["response"])

        assert cast(Any, response.is_closed) is True
