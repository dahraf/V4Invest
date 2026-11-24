# V4Invest — Product vision

**Positioning:** Investment Intelligence & Discovery Engine. Discover. Verify. Invest.

## Settled direction

- Iran-first, with no obligation to expand globally. Keep market, currency, calendar and instrument abstractions extensible.
- Public code repository; open-source/community-oriented development, subject to explicit license selection. Do not publish private data or unlicensed datasets.
- Reuse first: adopt reliable, permitted, maintained libraries and connectors instead of rebuilding standard capabilities. Prefer free/open-source options. Build the differentiating integration and intelligence layer ourselves.
- Search-first and research-first UX; Persian RTL, English LTR, local financial conventions and accessibility. Professional research workspaces, not a generic financial dashboard or signal feed.
- No live order execution in scope. Research outputs must be explainable, traceable and explicit about uncertainty.

## Primary users and jobs

Individual long-term investors: discover quality businesses, compare valuation, understand risk, maintain a watchlist, and see evidence changes. Professional analysts: inspect statements, assumptions, point-in-time data, corporate actions and reproducible computations. Developers/contributors: improve sources, adapters and validation via reviewable contributions.

## Product capabilities

| Capability | Value | Delivery status |
|---|---|---|
| V4Data | Collect, normalize, version and reconcile financial information | Experimental raw snapshot foundation only |
| V4Search | Symbol/company search, Persian aliases, filings, natural-language discovery | Planned |
| V4Verify | Evidence links, claim evaluation, conflicting-source detection | Planned |
| V4Score | Separate quality, valuation, growth, risk, liquidity and confidence metrics | Planned |
| V4Intel | Opportunity Radar, Investment Thesis, market relationships and scenarios | Planned |
| Research workspace | Company timelines, comparisons, watchlists and private portfolio analysis | Planned |
| Analyst intelligence | Timestamped forecasts and verified historical outcomes | Planned |
| Agent interface | Read-only API/MCP and model-independent research workflows | Planned |

## Differentiation

A query is a research workflow, not a chatbot answer: interpret intent → retrieve candidate instruments → apply reproducible criteria → verify evidence → explain inclusions/exclusions and uncertainty → preserve a dated thesis → monitor outcomes and changes. Treat analyst claims as leads, never primary facts. Independently evaluate system-generated forecasts as well.

Quality and price are separate. Score by sector and strategy. Do not rank when minimum data coverage is absent. Make missing and stale information visible. Use benchmark-relative total return and point-in-time datasets, not hindsight or selectively successful predictions.

## Success measures (targets, not current coverage)

- Instrument coverage: eligible active instruments captured / official eligible universe, by instrument type and market; target complete coverage subject to availability.
- Freshness: percentage of observations within source-specific SLA, with last-good timestamps and failures visible.
- Evidence coverage: percentage of displayed financial facts with source, period, unit and lineage; target 100%.
- Financial correctness: reconcile samples of normalized facts against primary filings; no unexplained material discrepancies at release.
- Search quality: judged Persian queries including aliases, spelling variants, ambiguity, criteria and relevant documents; measure precision@10 and recall on labeled test cases.
- Research quality: auditable formulas, explicit assumptions and limitations, benchmark-relative outcomes, and no fabricated evidence.

## Non-goals for MVP

Global equity coverage; paid data subscriptions; expensive distributed infrastructure; autonomous trading; indiscriminate scraping; full reproduction of third-party content; training models on restricted material; generic social engagement features.
