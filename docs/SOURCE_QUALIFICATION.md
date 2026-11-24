# Phase 1 — Source qualification, 2026-11-24

Status: documentation review only; no live adapter execution, package installation, source permission, or production certification.

## Evidence and shortlist

| Candidate | Documented coverage | Code license evidence | Role |
|---|---|---|---|
| [yfinance-ir](https://github.com/Fazel94/yfinance-ir) | TSETMC, Codal, TGJU, CPI; replayed offline fixtures documented | MIT per README | P0 Python integration candidate |
| [finpy-tse](https://github.com/ARahimiQuant/finpy-tse) | Historical/real-time TSE data | BSD-3-Clause per repository | P0 independent historical cross-check |
| [iran-bourse-mcp](https://github.com/msmahdinejad/iran-bourse-mcp) | Quotes, history, instruments, filings, market and commodity coverage | Pending direct license audit | P0 read-only research interface/reference |
| [codal-mcp](https://github.com/sepehr071/codal-mcp) | Filing search, statements, monthly activity, meeting decisions | Pending direct license audit | P0 disclosure parser candidate |
| [pytse-client](https://github.com/Glyphack/pytse-client) | Historical and intraday prices | Pending compatibility review | P1 comparison candidate |
| [iran-mcp](https://github.com/sepehr071/iran-mcp) | Catalog of Iranian data interfaces, including finance, laws and economic news | Review each component separately | P1 discovery catalog, not a bulk install |
| [iran-brokers-mcp](https://github.com/sepehr071/iran-brokers-mcp) | Public research/market endpoints of Mofid and Agah | Pending | P1 corroboration, never authenticated brokerage access |
| [tehran-market-data](https://github.com/Amir-Shokat/tehran-market-data) | Fund panel, NAV, ownership and price history | Pending | P1 fund and ownership candidate |
| [tse-market-data](https://github.com/BabakEslami/tse-market-data) | Community endpoint reference | Pending | Diagnostic reference only |
| [FundAI developer API](https://fundai.ir/developers) | Financial statements, market, sales, commodities | Commercial service terms and cost pending | Optional fallback; no subscription authorized |

Evidence: upstream public documentation, not an independent code or supply-chain audit. The yfinance-ir README documents offline tests and a separate live suite requiring Iranian network access. The iran-bourse-mcp [source guide](https://github.com/msmahdinejad/iran-bourse-mcp/blob/main/docs/DATA_SOURCES.md) distinguishes instrument IDs and data surfaces. Some tools use the same upstream endpoints; agreement across wrappers is not independent confirmation of underlying data. A [news report](https://www.tasnimnews.ir/fa/news/1404/10/06/3481080) describes a newer TSETMC REST service; obtain official access conditions directly before choosing between licensed service and community endpoint wrappers. No inference of API or redistribution permission from public accessibility or code license.

## Qualification matrix

Use a fixed public test universe (e.g. فملی، فولاد، وبملت، شپنا, one ETF, one rights instrument if currently listed). Include inactive/renamed tickers in historical coverage tests. No private holdings or user account data.

1. Pin exact upstream commit/version; inspect LICENSE and dependencies, execution paths, network destinations, telemetry, write actions, auth and update behavior. Reject unexpected side effects. No automatic installation of the whole catalog.
2. Record source terms, allowed acquisition/storage/AI use/redistribution, cost, rate limits and review date. Disabled until permissions and security checks pass; do not bypass CAPTCHA or access controls.
3. Run offline fixture tests first. If authorized, use bounded read-only live probes (one request per endpoint initially) from the intended environment; record UTC time, environment, HTTP status, latency, schema fingerprint, row count and failure state. No repeated traffic to a blocked endpoint.
4. Reconcile stable instrument IDs, market, units, trading dates, last and closing prices, and corporate actions against original exchange records. Compare adjusted and unadjusted returns explicitly. Verify multiple filing revisions, periods, currency/unit and consolidated vs standalone scopes against originals. Reject empty, HTML, stale and inconsistent responses.
5. Choose one primary and one fallback per capability based on demonstrated completeness, correctness, reliability, maintenance and resource cost. Use independent upstream sources when possible; distinguish wrapper fallback from upstream fallback.
6. Preserve public-safe evidence summaries and synthetic fixtures in Git; keep actual restricted response bodies and logs outside Git. Never mark an adapter enabled just because its README claims coverage.

## First vertical slice

Source review -> qualified instrument master -> daily prices -> filing discovery -> Persian symbol search -> one company evidence view. Keep SQLite and offline unit tests initially. Build deterministic normalization, provenance, stale/failure states and idempotency. Do not add a model provider, full MCP catalog, vector database, UI framework, paid infrastructure or live scheduling before requirements and qualification justify them.

## Research expansion

Discover FIPIRAN, IFB, IME, CBI, industry news and official issuer feeds. Qualify research/social sources individually; public profile URLs, dated claims and permitted citations only. Automated ingestion of Instagram/Telegram and video transcription remain disabled pending verified platform and content rights. Track claim outcomes against predeclared total-return benchmarks with point-in-time data.

## Status

No source admitted. No adapter certified. No code dependency adopted. No live probe results. License selection, upstream terms, runtime reachability, security and data redistribution remain open.
