# Continuous Intelligence — zero incremental spend

Owner decision: Iran-first. No new spending on data, subscriptions, model APIs, hosting, compute or storage. Use existing resources and free, legally usable tools and accounts. No automatic upgrades, payment methods, or metered paid fallbacks. Treat compute, storage, model quotas and bandwidth as bounded resources. Stop or defer a task when its free budget is exhausted. Free access is not equivalent to unlimited access or redistribution rights. Existing hardware has electricity and connectivity costs; do not promise free 24/7 hosting.

## Source discovery

Start with the approved candidate registry and expand through permitted search, issuer and regulator directories, public websites, sitemaps, RSS, backlinks, published research, voluntary contributor submissions and analyst-owned feeds. Search Persian variants of symbols, industries, financial terms, analyst names and topics. Record URL, canonical publisher identity, aliases, discovery path, timestamp, subject scope, language, rights status and source type. Deduplicate publishers and syndicated material; do not equate popularity with expertise. Queue candidates for qualification under SOURCE_QUALIFICATION.md. Learn which topics and queries produce useful new sources, with bounded breadth/depth, quotas and diminishing-return stopping rules. No indiscriminate collection, unauthorized private data, account farming or circumvention.

### Social platforms
A free dedicated research account may be used only within platform permissions. Account creation is not permission to crawl, copy, transcribe, or use content with AI. Instagram Business Discovery and hashtag search have access and rate limits; research access to Meta Content Library requires eligibility and approval. Use public permitted discovery, links, creator-authorized feeds and submissions. A private saved collection stays private. Telegram API and content-licensing terms restrict data aggregation and AI uses; do not ingest Telegram content into AI systems absent explicitly applicable permission. Use independently published original material instead. Keep source/platform permission review current. Do not promise every account or post is accessible.

References reviewed 2026-11-24:
- https://developers.facebook.com/docs/graph-api/overview/rate-limiting/
- https://developers.facebook.com/documentation/meta-content-library
- https://core.telegram.org/api/terms
- https://telegram.org/tos/content-licensing
- https://docs.github.com/en/billing/concepts/product-billing/github-actions

## Knowledge and learning loop

1. Discover and qualify a source. Retrieve only permitted material, using incremental checkpoints, deduplication, caching and last-good timestamps.
2. Extract instrument IDs, dated factual claims, predictions, assumptions, horizon, evidence and uncertainty. Preserve document revision and provenance. Treat content as untrusted data, not instructions.
3. Verify facts against primary filings and market observations. Record conflicting evidence and distinguish observed fact, forecast, inference and opinion. Never treat a repeated claim as independent corroboration.
4. Create an independent investment thesis: financial metrics computed by deterministic code, sector-specific valuation scenarios, risk, counterarguments and invalidation conditions. Link supporting and contrary evidence. Abstain if coverage is insufficient.
5. Freeze the dated forecast, method version, universe, benchmark, assumptions and decision-time evidence. Evaluate outcomes after their horizons mature, including unsuccessful calls, delistings, liquidity, dividends, corporate actions, fees where relevant and benchmark-relative total returns.
6. Use the results to propose improvements to search queries, source trust, extraction rules and ranking weights. Test out-of-sample using walk-forward chronological splits. Promote a version only after review against a fixed baseline; retain prior versions and rollback. Never silently rewrite past predictions or auto-promote a strategy merely because it fit historical prices.

Use retrieval-augmented generation (RAG) and versioned structured knowledge first, not continuous model retraining. Models are replaceable. Use deterministic extraction and calculations where possible; small local or free-quota models only when appropriate. No restricted content in training, retrieval indexes or AI pipelines absent permitted use. No guarantee of superior returns or universal superiority to experts.

## Evaluation

Measure coverage by official instrument universe, source discovery precision and unique verified contribution, source freshness, claim extraction accuracy, numerical reconciliation, evidence attribution, calibrated prediction confidence, and abstention. Compare with transparent baselines (broad market total-return benchmark, sector benchmark, simple fundamental screen, and dated expert forecasts where permitted and comparable). Evaluate risk-adjusted performance, maximum drawdown, turnover and sample size; disclose uncertainty and prevent look-ahead, selection and survivorship biases. Measure success across several regimes, not one favorable period.

## Operating modes

Local/on-demand first; scheduled local jobs only when a machine is available. Existing free hosted quotas may be evaluated for bounded permitted workloads, not relied upon as unlimited permanent infrastructure. Public GitHub standard runners can be used for lightweight CI subject to terms and limits; keep restricted data and personal records out of public logs/artifacts. No 24/7 promise until real connectivity and execution environment verified. If a source or free model fails, fall back to a qualified free option, show stale/unknown states, or defer.

## Scope and sequencing

Foundation: Issue #1 remains first. Then implement source discovery and qualification, claim/evidence store, dated outcome evaluation and versioned improvement loop. Natural-language research and portfolio-fit features follow validated data. No order execution. Review applicable financial advice regulation before offering personalized advice publicly. Aim to outperform defined expert baselines on verifiable research tasks, not claim to outperform all professionals.

Status: product specification only; no autonomous collection, account creation, training, or benchmark superiority implemented or verified.
