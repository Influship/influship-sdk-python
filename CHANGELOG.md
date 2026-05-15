# Changelog

## 0.1.0 (2026-05-15)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/Influship/influship-sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** add audience, brand alignment, key facts, vibe fields to creator response ([4c7bf09](https://github.com/Influship/influship-sdk-python/commit/4c7bf09985211ae6cb5c9784e8c60e186cf1f58f))
* **api:** add creator_kinds parameter to search.create method ([712759a](https://github.com/Influship/influship-sdk-python/commit/712759ae241285079b0060ff896dc25c5cb25237))
* **api:** add get_post/get_transcript methods to instagram, update post types ([c5d60ec](https://github.com/Influship/influship-sdk-python/commit/c5d60ec1b410ffcb49ece5ff68299d695ba9da36))
* **api:** add pagination to creators lookalike, extract MatchInfo type, fix cursor passing ([3be1022](https://github.com/Influship/influship-sdk-python/commit/3be10226051e066b82f26fd99170612908ddda3a))
* **api:** add raw resource with instagram/youtube endpoints ([d765413](https://github.com/Influship/influship-sdk-python/commit/d765413037084f7ad577d00b201a636a864c2f6b))
* **api:** add search_id/total fields, remove cursor param from search.create ([bbd32c2](https://github.com/Influship/influship-sdk-python/commit/bbd32c2e4391a9f31543862afed49f9fa9ca3d8a))
* **api:** remove source field from instagram transcript response types ([2c24026](https://github.com/Influship/influship-sdk-python/commit/2c240264f2abd9865713409ac1fb151f2479f261))
* **api:** update instagram profile and youtube channel/transcript responses ([8b83650](https://github.com/Influship/influship-sdk-python/commit/8b83650ce59ca2f00bb2b8c0f7f8005862a1849d))
* Fix Stainless pagination and model warnings in SDK config ([2ae3c29](https://github.com/Influship/influship-sdk-python/commit/2ae3c29275bfe74e3399f0ef0c0d950ae388531c))
* Fix timeout enforcement and migrate Instagram scraper to curl ([c1a121d](https://github.com/Influship/influship-sdk-python/commit/c1a121d337de698699c7dac5a1fb5814648083c9))
* **internal/types:** support eagerly validating pydantic iterators ([252fe69](https://github.com/Influship/influship-sdk-python/commit/252fe69b3d9652bb8ff9f2bf731d63006ec5b0af))
* **internal:** implement indices array format for query and form serialization ([b0fb922](https://github.com/Influship/influship-sdk-python/commit/b0fb922140eac09079b68be14a023d14a3f3a510))
* Remove app-level quota system and align billing/rate-limit enforcement with Stripe + Redis ([c7d8a60](https://github.com/Influship/influship-sdk-python/commit/c7d8a6012df2e31b92554e9a8374f1b3217bbe44))


### Bug Fixes

* **api:** make include parameter optional in creators retrieve method ([7dc834c](https://github.com/Influship/influship-sdk-python/commit/7dc834c23ef1d68df710b2de3baa996510c97b0d))
* **api:** move RawScraperError to shared types ([061b1e2](https://github.com/Influship/influship-sdk-python/commit/061b1e27385b033eb8966ebf8a02815b7dde26e4))
* **client:** add missing f-string prefix in file type error message ([cdd7fdb](https://github.com/Influship/influship-sdk-python/commit/cdd7fdb4104a72d2be89f7c6b48517abdb4285f4))
* **client:** preserve hardcoded query params when merging with user params ([77f87f2](https://github.com/Influship/influship-sdk-python/commit/77f87f2cca5dbacc34e894cf2c69e3f8f208842c))
* **deps:** bump minimum typing-extensions version ([1ebf842](https://github.com/Influship/influship-sdk-python/commit/1ebf84221a6cc9da7c4bcb414f47c4455f9b2dbe))
* ensure file data are only sent as 1 parameter ([76674d4](https://github.com/Influship/influship-sdk-python/commit/76674d4a000df97be89864108b9bf3923b4604f3))
* **pydantic:** do not pass `by_alias` unless set ([dba41e9](https://github.com/Influship/influship-sdk-python/commit/dba41e990d67482fc211cf0674e547c310a8eb26))
* sanitize endpoint path params ([825e363](https://github.com/Influship/influship-sdk-python/commit/825e363c5eb9b02a3e5fc5baa994fb711ea5cdab))
* **types:** remove model and provider from instagram transcript response types ([8944d7f](https://github.com/Influship/influship-sdk-python/commit/8944d7f405ad6e3597f397bebce7f13bc0df6fe3))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([eca9767](https://github.com/Influship/influship-sdk-python/commit/eca97676e9a6a75faf45ea3bea0b8eefeac55b8b))


### Chores

* **ci:** skip lint on metadata-only changes ([5ee4369](https://github.com/Influship/influship-sdk-python/commit/5ee43696849a917cf7a65f66a8b298ebbc4fa2e7))
* **ci:** skip uploading artifacts on stainless-internal branches ([2c985c8](https://github.com/Influship/influship-sdk-python/commit/2c985c8141c06115d531bc9293bb1291a3d04d45))
* **internal:** add request options to SSE classes ([fa680d0](https://github.com/Influship/influship-sdk-python/commit/fa680d005639f7836e614b03c165791f1c64c0b3))
* **internal:** codegen related update ([6ed3406](https://github.com/Influship/influship-sdk-python/commit/6ed3406334c705ae2278a09a040b916c0432d9ae))
* **internal:** codegen related update ([a7d0c03](https://github.com/Influship/influship-sdk-python/commit/a7d0c03f03bae935f64b076c211d283ad9069495))
* **internal:** make `test_proxy_environment_variables` more resilient ([1775e30](https://github.com/Influship/influship-sdk-python/commit/1775e30216baabb1affe64be26b9455a35bc7a30))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([2042983](https://github.com/Influship/influship-sdk-python/commit/20429833fae8ecd9dbe6eee1d140cdb9e0763260))
* **internal:** more robust bootstrap script ([09db9ca](https://github.com/Influship/influship-sdk-python/commit/09db9caf00714de6ccb7eccd314c0a903b6ea55f))
* **internal:** refactor Instagram response types to shared models, fix address_json type ([1ce31a9](https://github.com/Influship/influship-sdk-python/commit/1ce31a9406b653b08e333139febfb5acb01ca641))
* **internal:** reformat pyproject.toml ([c63d362](https://github.com/Influship/influship-sdk-python/commit/c63d362a824ea0145bb90d8be4e493463d32028c))
* **internal:** regenerate SDK with no functional changes ([2f56132](https://github.com/Influship/influship-sdk-python/commit/2f561321662c817f965ff9d4ad61e3b13f15de38))
* **internal:** tweak CI branches ([5eea6ab](https://github.com/Influship/influship-sdk-python/commit/5eea6ab384a360852d54e5617e92e0d8d090a12e))
* **internal:** update gitignore ([a47bc6c](https://github.com/Influship/influship-sdk-python/commit/a47bc6c615c786a620fad78eafb31927cbecc718))
* update Stainless production repos to influship org ([f92ef39](https://github.com/Influship/influship-sdk-python/commit/f92ef39428d669160509c279e52deb10343e2b2c))


### Documentation

* **api:** add MCP tool references to creators/posts/profiles/search methods ([fb75a8e](https://github.com/Influship/influship-sdk-python/commit/fb75a8eedb6c1e86edb35b94e82d0eb27b9f4537))
* **api:** correct profile to channel terminology in youtube channel method ([a8f561f](https://github.com/Influship/influship-sdk-python/commit/a8f561fde0da698d26689d699c394cbcb3475f8d))
* **api:** update instagram method docstrings ([9d881aa](https://github.com/Influship/influship-sdk-python/commit/9d881aadfbbc7d742d739042a96c973a9824573f))
* **api:** update pricing documentation across creators/posts/profiles/raw/search ([b82801e](https://github.com/Influship/influship-sdk-python/commit/b82801e0c5cc55dc0509e3a8ac412518ca9745ce))
* **internal:** update MCP server package name in installation links ([7d78559](https://github.com/Influship/influship-sdk-python/commit/7d78559d721175e453eea56d8fab60a0f4c9a229))
* update examples ([53aa0d6](https://github.com/Influship/influship-sdk-python/commit/53aa0d622795bdc2076f69d67ac51525b814f7d6))
