# Roadmap and delivery gates

No calendar estimates or feature completion claims without evidence. The public repository is initialized; license selection is pending. Existing prototype has raw snapshots and experimental request adapters; no real market database or UI.

| Phase | Deliverable | Release gate |
|---|---|---|
| 0 Foundation | Public repository, vision, architecture, data policy, source inventory, starter tests | Review public-safe contents and select license; repository initialized |
| 1 Source qualification | Source discovery, rights review, tool benchmark, primary and fallback adapter choice | Documented permission and live sample evidence; test fixtures; failures visible |
| 2 Data core | Instrument master, daily market history, filings, financial facts, corporate actions | Reconcile identifiers/units and cross-sector samples; no silent duplicates/staleness |
| 3 Discovery MVP | Persian symbol and document search, company page, filters, comparison, watchlist | Search relevance evaluation; sources and freshness visible; basic accessible RTL/LTR UI |
| 4 Investment intelligence | Sector-aware metrics, V4Score, valuation, risk, opportunity radar, scenarios | Reproducible calculations, missingness gates, point-in-time tests and benchmark validation |
| 5 Research intelligence | Permitted news/social sources, claims, analysts, company timeline, thesis and outcomes | Evidence provenance and uncertainty, no selective forecast evaluation |
| 6 Personal workspace | Private portfolio imports, exposures, benchmark comparison, strategy profiles | Isolation, permission checks, privacy review and reconciliation |
| 7 Delivery and operations | Read-only API/MCP, scheduling, alerts, monitoring, backup/restore, UI hardening | Operational validation and security/quality review |
| 8 Ecosystem | Contributor workflow, community sources, extension SDK, documented API | License and data rights compliance; stable contracts and contributor tests |

Global securities expansion is optional, not a success criterion. Relevant global macro series can enter earlier. Begin with deterministic research and a small functional vertical slice rather than waiting for every source to be integrated.

## P0 backlog for Codex / Work

1. Audit starter code and repository contents; verify no personal data, credentials, raw third-party documents or databases are shipped. Document gaps.
2. Review source terms and access, benchmark existing collectors (do not indiscriminately install dependencies); record actual availability from chosen execution environment, API status and schema samples.
3. Define instrument and fact contracts, migrations, run logs, timestamps, permissions, rate limit and freshness states; implement with test-first changes.
4. Add validated fixture-based TSETMC/Codal ingestion and identity mapping; implement pagination, report revision handling and bounded incremental checkpoints. Quarantine mismatches.
5. Collect authorized small real samples, cross-check against official evidence, and publish a coverage and data-quality report without exposing restricted data.
6. Add a minimal offline Persian symbol search over normalized instrument records, then a read-only query interface; evaluate representative ambiguous/alias queries.
7. Decide operational storage and scheduling based on measurements; no paid or difficult-to-reverse decisions without approval.

Keep one repository and minimal CI. Prefer small focused tests and offline fixtures; add controlled live integration only after admission checks. All phases distinguish proposed, implemented, tested, integrated and operationally verified.
