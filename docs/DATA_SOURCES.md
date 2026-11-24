# Sources and tool discovery

The machine-readable initial registry is `config/sources.json`. It is a candidate inventory, not proof of live access, accuracy, API support, licensing, free pricing, or permission to collect. Expand coverage via official directories, issuer disclosures, licensed advisors, sector publications, search and contributor submissions. Check deduplicated identity and ownership, including impersonation risks.

## Source hierarchy

1. Official exchanges, regulator, Codal, TSETMC, FIPIRAN, central bank, statistics center and official commodity sources for facts.
2. Issuer reports and original research for context, then verified commercial/reference data for reconciliation.
3. Economic media and sector news for event discovery.
4. Analysts, social/video and podcasts for hypotheses and claim tracking; never substitute these for primary financial data.
5. Global commodities and macro drivers relevant to Iran; no requirement for full foreign equity coverage.

## Admission lifecycle

`candidate → identity/terms reviewed → technical probe authorized → real fixture reviewed → validated → enabled` (or `blocked`, `paused`, `retired`). Record owner, canonical URL, category, scope, permitted access/retention/redistribution/AI use, cost, timestamp, update frequency, schema, rate limits, provenance, network reachability, coverage, failures, alternates and last review. Unknown rights or failure means disabled. Live verification requires actual test evidence, not a successful HTTP status alone.

## Reuse-first tool assessment

Evaluate candidates by overlap with needed endpoints, license compatibility, maintenance/release cadence, security and dependency review, ability to run offline tests, network behavior, correctness on a fixed sample, runtime cost, failure visibility and replaceability. Do not adopt based on stars or README promises alone. Select at most one primary and one useful fallback per capability where practical. Use an adapter interface to avoid lock-in. Run small fixture-backed tests first; live checks opt-in and limited to authorized requests.

## Initial evaluation order

- TSETMC: instrument identity and market-watch data, then history and corporate actions; compare `pytse-client`, `finpy-tse` and selected modern multi-source candidates.
- Codal: disclosure discovery and pagination, report versions, then actual financial statements and monthly activity. Verify Persian labels, scale, period and consolidated/standalone scope.
- FIPIRAN and exchange sources: fund identity/NAV and official instrument coverage.
- Macro and sector feeds: separate exchange rate types, dates, currencies and revisions.
- Research/analyst sources: official feeds, permitted document access, links and timestamped claims. Assess five public Instagram profile candidates without storing private saved collection data. Video transcription only when permitted.

## Source scorecard (not yet scored)

Data authority, coverage, timeliness, observed accuracy, availability, clear permissions, cost, and implementation effort. Rights and security are hard admission gates rather than compensable scores. Store measurement evidence and dates. Analyst credibility is separate from provider reliability; measure explicit dated predictions, failures as well as successes, adjusted returns versus predeclared benchmarks, and coverage/survivorship bias.

## First implementation task

Produce a real capability matrix and authorized sample observations for TSETMC and Codal. Confirm terms; perform bounded read-only requests only after review; report unavailable/blocked sources instead of bypassing. Add fixtures and normalize a cross-sector sample. Reconcile against primary records. Only then enable scheduling or historical backfill. A candidate registry alone does not meet acceptance.
