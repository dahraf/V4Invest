# V4Invest

**Discover. Verify. Invest.**

An evidence-first investment search and discovery engine for Iran's capital market. V4Invest aims to combine trustworthy financial data, market intelligence, independent research and transparent opportunity ranking. Iran-first; market-neutral identifiers and adapter contracts leave room for other markets without committing to global coverage.

## Status — foundation prototype

This is the public repository `dahraf/V4Invest`. The open-source license remains to be selected by the owner. This is not a production service.

Implemented in the foundation: local SQLite snapshot storage, deduplication, observation history, JSON import, experimental read-only TSETMC and Codal adapters, and offline tests. The source registry contains research candidates, not certified providers. An offline Persian instrument catalog is also implemented for explicitly normalized imports; see [offline catalog](docs/OFFLINE_CATALOG.md). Live collection, source rights, market-wide coverage, financial scoring, and AI are not yet validated or implemented. No real portfolio or market observations are bundled.

## Local development (Python 3.11+, standard library)

```sh
python -m unittest discover -s tests -v
python -m v4invest init
python -m v4invest status
```

Experimental collection is opt-in, and must only be used after access and use conditions are reviewed. These endpoints are not guaranteed supported APIs. Codal currently retrieves the first search page, not financial statements. TSETMC retrieves a market-watch snapshot. Neither collector is certified for scheduling.

```sh
# After source access approval and a controlled integration check:
python -m v4invest collect tsetmc
python -m v4invest collect codal --symbol فملی
```

Import authorized public JSON with explicit provenance:

```sh
python -m v4invest import-json source.json --source example --url https://example.com/data --retrieved-at 2026-11-24T12:00:00+03:30
```

## Project documents

- [Product vision](docs/PRODUCT_VISION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Source and tool evaluation](docs/DATA_SOURCES.md)
- [Data rights and privacy](docs/DATA_GOVERNANCE.md)
- [Development instructions](AGENTS.md)
- [Candidate registry](config/sources.json)
- [Offline catalog](docs/OFFLINE_CATALOG.md)
- [Source qualification](docs/SOURCE_QUALIFICATION.md)
- [Continuous intelligence](docs/CONTINUOUS_INTELLIGENCE.md)
- [Technology discovery](docs/TECHNOLOGY_DISCOVERY.md)

Public code does not imply unrestricted redistribution of provider data. Keep private portfolios, credentials, restricted content, and local database files outside Git. V4Invest supports research and informed decisions, not brokerage order execution.
