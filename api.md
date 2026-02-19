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
from influship.types import SearchQueryResponse
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/influship/resources/search.py">query</a>(\*\*<a href="src/influship/types/search_query_params.py">params</a>) -> <a href="./src/influship/types/search_query_response.py">SearchQueryResponse</a></code>

# Profiles

Types:

```python
from influship.types import ProfileGetResponse, ProfileLookupResponse
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

- <code title="get /v1/posts">client.posts.<a href="./src/influship/resources/posts.py">list</a>(\*\*<a href="src/influship/types/post_list_params.py">params</a>) -> <a href="./src/influship/types/post_list_response.py">PostListResponse</a></code>

# BrandSafety

Types:

```python
from influship.types import (
    BrandSafetyAnalyzeCreatorsResponse,
    BrandSafetyAnalyzePostsResponse,
    BrandSafetyAnalyzeProfilesResponse,
)
```

Methods:

- <code title="post /v1/brand-safety/creators">client.brand_safety.<a href="./src/influship/resources/brand_safety.py">analyze_creators</a>(\*\*<a href="src/influship/types/brand_safety_analyze_creators_params.py">params</a>) -> <a href="./src/influship/types/brand_safety_analyze_creators_response.py">BrandSafetyAnalyzeCreatorsResponse</a></code>
- <code title="post /v1/brand-safety/posts">client.brand_safety.<a href="./src/influship/resources/brand_safety.py">analyze_posts</a>(\*\*<a href="src/influship/types/brand_safety_analyze_posts_params.py">params</a>) -> <a href="./src/influship/types/brand_safety_analyze_posts_response.py">BrandSafetyAnalyzePostsResponse</a></code>
- <code title="post /v1/brand-safety/profiles">client.brand_safety.<a href="./src/influship/resources/brand_safety.py">analyze_profiles</a>(\*\*<a href="src/influship/types/brand_safety_analyze_profiles_params.py">params</a>) -> <a href="./src/influship/types/brand_safety_analyze_profiles_response.py">BrandSafetyAnalyzeProfilesResponse</a></code>
