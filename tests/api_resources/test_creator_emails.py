# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from influship import Influship, AsyncInfluship
from tests.utils import assert_matches_type
from influship.types import CreatorEmailLookupResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreatorEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: Influship) -> None:
        creator_email = client.creator_emails.lookup(
            creators=[{"creator_id": "123e4567-e89b-12d3-a456-426614174000"}],
        )
        assert_matches_type(CreatorEmailLookupResponse, creator_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: Influship) -> None:
        response = client.creator_emails.with_raw_response.lookup(
            creators=[{"creator_id": "123e4567-e89b-12d3-a456-426614174000"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator_email = response.parse()
        assert_matches_type(CreatorEmailLookupResponse, creator_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: Influship) -> None:
        with client.creator_emails.with_streaming_response.lookup(
            creators=[{"creator_id": "123e4567-e89b-12d3-a456-426614174000"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator_email = response.parse()
            assert_matches_type(CreatorEmailLookupResponse, creator_email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreatorEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncInfluship) -> None:
        creator_email = await async_client.creator_emails.lookup(
            creators=[{"creator_id": "123e4567-e89b-12d3-a456-426614174000"}],
        )
        assert_matches_type(CreatorEmailLookupResponse, creator_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncInfluship) -> None:
        response = await async_client.creator_emails.with_raw_response.lookup(
            creators=[{"creator_id": "123e4567-e89b-12d3-a456-426614174000"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        creator_email = await response.parse()
        assert_matches_type(CreatorEmailLookupResponse, creator_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncInfluship) -> None:
        async with async_client.creator_emails.with_streaming_response.lookup(
            creators=[{"creator_id": "123e4567-e89b-12d3-a456-426614174000"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            creator_email = await response.parse()
            assert_matches_type(CreatorEmailLookupResponse, creator_email, path=["response"])

        assert cast(Any, response.is_closed) is True
