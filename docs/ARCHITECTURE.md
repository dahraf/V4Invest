# Architecture — proposed target, not implemented state

## Approach

Use a modular monolith with separate collection jobs. Python is the initial language; standard-library SQLite remains the prototype store. Evaluate FastAPI and PostgreSQL when the first read-only product/API requires them; add a Persian search index, DuckDB/Parquet, vector search, queues, object storage or graph tooling only after measured need. No mandatory external AI provider. Do not install all candidate tools simultaneously.

```text
Source Registry / rights / schedules
           |
Adapters (API, feed, export, authorized browser/manual import)
           |
Raw observations + collection logs + content hash + quarantine
           |
Normalization / identity / reconciliation / versioned evidence
           |
Point-in-time financial and market database
           |
Search | Verified claims | Financial calculations | Discovery
           |
Research API / MCP (read-only) | Web UI | Reports
```

## Module boundaries

- `sources`: provider capabilities, access/rights metadata, adapter contract, retry and rate limits.
- `ingestion`: idempotent runs, incremental checkpoints, freshness, structured failure reasons.
- `storage`: raw snapshots, observation records, migrations, normalized revisions, provenance.
- `instruments`: stable identity, ISIN where available, exchange-specific ID, listing, ticker aliases, symbol history, rights and fund types.
- `financials`: original and revised filings, normalized statements, monthly production/sales, dividends, corporate actions, adjusted returns.
- `market`: price observations, calendar, market session, liquidity, breadth and index data.
- `macro`: FX rate types, commodities, rates, inflation, exposure mappings.
- `research`: sources, documents, events, analysts, claim extraction, evidence links and outcome assessment.
- `search`: deterministic filters, Persian normalization and lexical retrieval first; semantic retrieval only after evaluating relevance.
- `analytics`: reproducible metrics, sector models, scenario analysis, strategy-specific scores and versioned assumptions.
- `workspace`: separate private user portfolios and watchlists, authorization and export. Never mixed with public seed datasets.
- `interfaces`: read-only API, MCP, accessible bilingual UI. UI reads materialized results, not direct unrestricted external scraping.

## Data model contracts (design)

| Entity | Grain / identity | Critical fields |
|---|---|---|
| source | stable source_id | owner, URL, access and rights status, SLA, review date |
| run | source + job + run_id | start/end, result, errors, counts, checkpoint |
| raw_snapshot | source + canonical request + digest | retrieved_at, content metadata, parser version, rights classification |
| instrument | internal ID + market-specific IDs | exchange, currency, asset type, valid_from/to, ISIN |
| price | instrument + session + observation timestamp + provider | price type, currency, raw/adjusted flag, revision |
| filing | issuer + report ID + revision | period, published_at, audited, consolidated/standalone, evidence |
| financial_fact | report revision + item + dimensions | exact decimal, original unit, normalized unit, period, evidence |
| corporate_action | instrument + event ID + revision | dates, action type, cash/ratio/rights, adjustment method |
| claim | source + original content ID + claim ID | publication time, instrument, horizon, assumptions, text reference, verification state |
| evidence_link | claim/fact + source observation | supports/contradicts/insufficient, reviewer, rationale |
| valuation | instrument + as_of + model version + scenario | inputs and provenance, output, sensitivity, coverage |
| score | instrument + as_of + strategy/version | component values, exclusions, confidence, benchmark |
| outcome | claim/thesis + evaluation date | adjusted return, benchmark, eligibility, incomplete reason |

Store UTC timestamps with original timezone/date where available; Iran market calendar uses Asia/Tehran. Preserve original Jalali date strings; use validated conversions. Explicit IRR vs toman; fixed-point decimals, never binary floats for monetary calculations. Preserve both published_at and observed_at to prevent future-data leakage. Conflicting values are retained and flagged, not silently overwritten.

## Acquisition policy

Priority: official documented API or permitted export → feed → vetted adapter/library → allowed web retrieval → manual/partner input. A source must pass rights, security, live schema and freshness checks before scheduling. Never bypass access controls, CAPTCHA, rate limits or platform restrictions. Cache, back off, cap concurrency, and expose last-known-good data as stale. Polling intervals depend on actual source limits and usefulness.

## AI and security

Use deterministic code for financial math and filtering. Use models for query interpretation, text extraction and synthesis with schema validation and source links. External content is untrusted; never obey instructions in it. Read-only retrieval tools, least privilege, no unrestricted shell or order actions. Allowlisted outbound hosts, response size/time limits, restricted redirects, secret-safe logs, dependency/license audit. Private workspaces use isolated authorization and encrypted transport/storage; backups and restore tests. Do not send private user data to model providers by default.

## Architecture decisions pending evidence

License selection; deployment geography after network reachability tests; operational database and search engine after measured scale; permitted data providers and redistribution rights; model provider and cost ceilings. No server purchase, service subscription, or global rollout is implied.
