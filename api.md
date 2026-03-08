# Shared Types

```python
from influship.types import CreatorBasic, ProfileSummary
```

# Health

Types:

```python
from influship.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/influship/resources/health.py">check</a>() -> <a href="./src/influship/types/health_check_response.py">HealthCheckResponse</a></code>

# Creators

Types:

```python
from influship.types import (
    CreatorRetrieveResponse,
    CreatorAutocompleteResponse,
    CreatorLookalikeResponse,
    CreatorMatchResponse,
)
```

Methods:

- <code title="get /v1/creators/{id}">client.creators.<a href="./src/influship/resources/creators.py">retrieve</a>(id, \*\*<a href="src/influship/types/creator_retrieve_params.py">params</a>) -> <a href="./src/influship/types/creator_retrieve_response.py">CreatorRetrieveResponse</a></code>
- <code title="get /v1/creators/autocomplete">client.creators.<a href="./src/influship/resources/creators.py">autocomplete</a>(\*\*<a href="src/influship/types/creator_autocomplete_params.py">params</a>) -> <a href="./src/influship/types/creator_autocomplete_response.py">CreatorAutocompleteResponse</a></code>
- <code title="post /v1/creators/lookalike">client.creators.<a href="./src/influship/resources/creators.py">lookalike</a>(\*\*<a href="src/influship/types/creator_lookalike_params.py">params</a>) -> <a href="./src/influship/types/creator_lookalike_response.py">CreatorLookalikeResponse</a></code>
- <code title="post /v1/creators/match">client.creators.<a href="./src/influship/resources/creators.py">match</a>(\*\*<a href="src/influship/types/creator_match_params.py">params</a>) -> <a href="./src/influship/types/creator_match_response.py">CreatorMatchResponse</a></code>

# Search

Types:

```python
from influship.types import SearchCreateResponse, SearchRetrieveResponse
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/influship/resources/search.py">create</a>(\*\*<a href="src/influship/types/search_create_params.py">params</a>) -> <a href="./src/influship/types/search_create_response.py">SearchCreateResponse</a></code>
- <code title="get /v1/search/{id}">client.search.<a href="./src/influship/resources/search.py">retrieve</a>(id, \*\*<a href="src/influship/types/search_retrieve_params.py">params</a>) -> <a href="./src/influship/types/search_retrieve_response.py">SyncQueryCursor[SearchRetrieveResponse]</a></code>

# Profiles

Types:

```python
from influship.types import (
    ProfileActivity,
    ProfileGrowth,
    ProfileMetrics,
    ProfileResponseData,
    ProfileGetResponse,
    ProfileLookupResponse,
)
```

Methods:

- <code title="get /v1/profiles/{platform}/{username}">client.profiles.<a href="./src/influship/resources/profiles.py">get</a>(username, \*, platform) -> <a href="./src/influship/types/profile_get_response.py">ProfileGetResponse</a></code>
- <code title="post /v1/profiles/lookup">client.profiles.<a href="./src/influship/resources/profiles.py">lookup</a>(\*\*<a href="src/influship/types/profile_lookup_params.py">params</a>) -> <a href="./src/influship/types/profile_lookup_response.py">ProfileLookupResponse</a></code>

# Posts

Types:

```python
from influship.types import PostListResponse
```

Methods:

- <code title="get /v1/posts">client.posts.<a href="./src/influship/resources/posts.py">list</a>(\*\*<a href="src/influship/types/post_list_params.py">params</a>) -> <a href="./src/influship/types/post_list_response.py">SyncQueryCursor[PostListResponse]</a></code>

# Raw

## Instagram

Types:

```python
from influship.types.raw import InstagramGetProfileResponse
```

Methods:

- <code title="get /v1/raw/instagram/profile/{username}">client.raw.instagram.<a href="./src/influship/resources/raw/instagram.py">get_profile</a>(username, \*\*<a href="src/influship/types/raw/instagram_get_profile_params.py">params</a>) -> <a href="./src/influship/types/raw/instagram_get_profile_response.py">InstagramGetProfileResponse</a></code>

## Youtube

Types:

```python
from influship.types.raw import (
    TranscriptSegment,
    YoutubeGetChannelResponse,
    YoutubeGetChannelTranscriptsResponse,
    YoutubeGetTranscriptResponse,
    YoutubeSearchResponse,
)
```

Methods:

- <code title="get /v1/raw/youtube/channel/{handle}">client.raw.youtube.<a href="./src/influship/resources/raw/youtube.py">get_channel</a>(handle, \*\*<a href="src/influship/types/raw/youtube_get_channel_params.py">params</a>) -> <a href="./src/influship/types/raw/youtube_get_channel_response.py">YoutubeGetChannelResponse</a></code>
- <code title="get /v1/raw/youtube/channel-transcripts/{handle}">client.raw.youtube.<a href="./src/influship/resources/raw/youtube.py">get_channel_transcripts</a>(handle, \*\*<a href="src/influship/types/raw/youtube_get_channel_transcripts_params.py">params</a>) -> <a href="./src/influship/types/raw/youtube_get_channel_transcripts_response.py">YoutubeGetChannelTranscriptsResponse</a></code>
- <code title="get /v1/raw/youtube/transcript/{video_id}">client.raw.youtube.<a href="./src/influship/resources/raw/youtube.py">get_transcript</a>(video_id, \*\*<a href="src/influship/types/raw/youtube_get_transcript_params.py">params</a>) -> <a href="./src/influship/types/raw/youtube_get_transcript_response.py">YoutubeGetTranscriptResponse</a></code>
- <code title="get /v1/raw/youtube/search">client.raw.youtube.<a href="./src/influship/resources/raw/youtube.py">search</a>(\*\*<a href="src/influship/types/raw/youtube_search_params.py">params</a>) -> <a href="./src/influship/types/raw/youtube_search_response.py">YoutubeSearchResponse</a></code>
