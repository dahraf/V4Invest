# Technology Discovery — 2026-11-24

Status: public documentation assessment, not installation, code audit, benchmark execution, or production certification. Recommendations are candidates, not authorization to adopt dependencies. Issue #1 remains the first delivery gate; #2 owns continuous intelligence. No new spending, no paid fallback.

## Decision matrix

| Candidate and upstream evidence | Intended use | Decision and gate |
|---|---|---|
| [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot), [NOTICE](https://github.com/AI4Finance-Foundation/FinRobot/blob/master/NOTICE) | financial research workflow, scenarios, reports | Adapt patterns; Apache-2.0 documented, commercial FMP and other provider dependencies not authorized. Evaluate local model support and remove US-market assumptions. |
| [OpenBB](https://github.com/OpenBB-finance/OpenBB), [versioned license FAQ](https://github.com/OpenBB-finance/openbb-docs/blob/main/content-odp/python/faqs/license.mdx) | provider abstraction and typed data interfaces | Adapt architecture; V5 documentation states Apache-2.0, V4 AGPL. Audit exact version and provider terms. Do not fork full platform. |
| [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) | financial text classification and methodology | Reference; MIT code, individual data/model rights separate. No fine-tuning before evidence that retrieval and deterministic extraction are inadequate. |
| [Qlib](https://github.com/microsoft/qlib) | quantitative research, backtesting, factor evaluation | Defer until point-in-time Iran dataset and total-return corporate-action handling are validated. |
| [RD-Agent](https://github.com/microsoft/RD-Agent) | research automation | Defer; evaluate sandboxing, token/compute costs, time-split leakage and reproducibility. No autonomous code execution or strategy promotion in production. |
| [Awesome AI4Finance](https://github.com/AI4Finance-Foundation/Awesome_AI4Finance) | technology discovery | Reference catalog only; no automatic dependency install. |
| [FinanceBench](https://github.com/patronus-ai/financebench) | grounded financial QA evaluation | Adapt evaluation design, review dataset rights; not a Persian or Iran-market test. |
| [FinMRAGBench](https://aclanthology.org/2026.findings-acl.187/) | multimodal cross-page/document evidence QA | Adapt evaluation design; 887 expert-verified QA pairs documented in paper; evaluate actual licensed dataset separately. |
| [iran-bourse-mcp](https://github.com/msmahdinejad/iran-bourse-mcp), [sources](https://github.com/msmahdinejad/iran-bourse-mcp/blob/main/docs/DATA_SOURCES.md) | read-only MCP and Iranian market instrument/quote/filing reference | P0 qualification; independent underlying evidence needed, not simply two wrappers agreeing. |
| [yfinance-ir](https://github.com/Fazel94/yfinance-ir) | Python ingestion of TSETMC, Codal, TGJU, CPI | P0 qualification; upstream documents offline fixtures. Pin and test exact release; review data access terms. |
| [codal-mcp](https://github.com/sepehr071/codal-mcp) | structured financial statement tables, activity and filing discovery | P0 qualification; compare units, periods, table revisions and reported amounts with original filings. |
| [finpy-tse](https://github.com/ARahimiQuant/finpy-tse) | history, adjusted returns | P0 cross-check candidate; BSD-3-Clause documented; verify adjustment convention. |
| [iran-mcp](https://github.com/sepehr071/iran-mcp) | discovery catalog for local financial, policy, news and other providers | Reference only; individually qualify selected servers, no bulk installation. |
| [iran-brokers-mcp](https://github.com/sepehr071/iran-brokers-mcp) | public broker research and market data | P1; no authenticated brokerage access or order execution. |
| [iranquant](https://github.com/dadjoyan/iranquant) | async SDK | Hold: README mentions insecure transport fallback after SSL/connect errors. Inspect exact implementation; do not disable TLS verification or downgrade security. |
| [pytse-client](https://github.com/Glyphack/pytse-client), [tehran-market-data](https://github.com/Amir-Shokat/tehran-market-data) | historical data and fund/ownership coverage | Retain candidates; not newly verified in this pass. |
| [SearXNG](https://github.com/searxng/searxng) | metasearch and discovery | Prototype only, upstream access, quotas, terms and deployment overhead apply; not a complete web index or unlimited free search API. |
| [Trafilatura](https://github.com/adbar/trafilatura) | permitted article text and metadata | Prioritize small extraction benchmark; RSS/sitemaps before large crawls. |
| [Scrapy](https://github.com/scrapy/scrapy) | structured crawling | Conditional when simple feeds insufficient; per-source rights/rate limits, bounded queues and domain allowlists. |
| [Playwright](https://github.com/microsoft/playwright) | authorized dynamic page access and UI testing | Last resort for acquisition; no circumventing access controls, login challenges or CAPTCHA. |
| [Docling](https://github.com/docling-project/docling) | document layout, tables and reading order | Conditional local benchmark on permitted Persian statements; MIT code documented; separately inspect model licenses and CPU/RAM. Prefer native HTML/XLSX/JSON over OCR. |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | permitted media transcription | Optional; CPU INT8 documented, measure Persian accuracy and speed before adopting. |
| [Hazm](https://github.com/roshan-research/hazm) | Persian text normalization | Candidate; compare lightweight explicit alias/Unicode rules first. Preserve original text and tickers, digits, signs and units. |
| [persian-rag](https://github.com/sadrmanesh/persian-rag) | Persian normalization, hybrid retrieval and evaluation | Evaluate small isolated benchmark rather than whole pipeline adoption. |
| [Yalda Embedding](https://github.com/yaldat/yalda-embedding) | Persian semantic retrieval | Candidate; README describes Qwen3-Embedding-0.6B base, 595.8M parameters. Direct page fetch failed; weights, license and runtime unverified. |
| [Hakim](https://huggingface.co/MCINext/Hakim) | Persian embeddings | Hold until model weights, commercial/use license and local execution verified; direct fetch returned HTTP 429. Do not infer rights from model availability. |
| [Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) | multilingual retrieval baseline | Candidate Apache-2.0 model card; compare with Persian models and lexical-only baseline before adoption. |
| [SQLite FTS5](https://www.sqlite.org/fts5.html) | local full-text search | Proposed MVP default; test build availability and Persian normalization; no separate search service. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | local quantized inference | Optional benchmark on existing hardware; no mandatory LLM for ingestion or arithmetic. |
| [DuckDB](https://github.com/duckdb/duckdb), [Polars](https://github.com/pola-rs/polars) | analytical queries and transformations | Defer dependency until measured data-volume or computation need. |
| Ollama, Sentence Transformers, VectorBT, Backtrader | local inference, retrieval or backtesting alternatives | Retain as future candidates; no comparative execution or current license audit in this pass. |
| [GitHub Actions billing](https://docs.github.com/en/actions/concepts/billing-and-usage) | lightweight tests | Public standard runners free subject to applicable rules; avoid paid larger runners, storage overages or using CI as a persistent service. |

## V4FinanceBench proposal

Build a Persian financial research benchmark, not an advertised investment-performance guarantee. Start with independently checked, licensed/synthetic examples: symbol identity and aliases; rial/toman and original statement scales; fiscal periods and restatements; deterministic arithmetic; report/table evidence; claims with conflicting or missing evidence; source freshness; sector-specific valuation; risk exposures. Include adversarial prompt-injection content and abstention cases. Preserve original evidence and publication dates where allowed.

Suggested initial 60 cases: 15 identity/search, 15 numerical/units/periods, 15 document/claim evidence, 10 risk and valuation methodology, 5 abstention/security. These are targets, not existing test counts. Compare exact match or tolerance for numeric answers, retrieval recall@k, precision@k, citation correctness, abstention, latency, memory and incremental cost. Use chronological held-out sets for forecast tests, never train on held-out material; benchmark-relative adjusted total returns and risk require validated historical datasets.

## Implementation sequence and decision rationale

1. Keep issue #1: source rights/security qualification, deterministic normalized instrument/price/filing storage, verified small samples and minimal Persian search. Prefer SQLite and lexical retrieval; no model requirement.
2. Add source discovery and claim/evidence store under #2. Start with official directories, permitted RSS/sites and explicit source metadata, not unrestricted social scraping. Restrict outbound hosts, redirects, size, quotas; guard prompt injection.
3. Establish V4FinanceBench before semantic search or research AI. Evaluate lexical baseline, then optional local embedding; promote only if evidence quality improves at acceptable resource cost.
4. Add independent Bull/Bear/valuation/risk review with deterministic computation and dated thesis, adapting FinRobot patterns where appropriate. Use a single model with structured tasks rather than expensive agent swarms.
5. Evaluate Qlib and RD-Agent after usable historical point-in-time data; no automated order execution.

V4Radar maps to source/opportunity discovery; V4Knowledge and V4Memory to versioned evidence; V4Lab to evaluation and scenarios; V4Audit to verification; V4Academy to licensed research methodology. These are responsibilities inside one modular monolith, not additional services or requirements to install frameworks.

## Unresolved and safety gates

No source admitted or dependency installed by this document. No live access, Persian accuracy, latency, actual zero-cost uptime or license compatibility certified. Direct Hakim/Yalda fetch failures and iranquant insecure-fallback concern remain. Free accounts may be used only as authorized by the owner and platform. Review source permissions, content licensing, exact dependency versions, security and financial-advice obligations before any public production use. Do not claim superior investment results without out-of-sample evidence.
