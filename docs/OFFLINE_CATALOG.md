# Offline instrument catalog

Partial delivery of #1. This catalog imports an explicitly normalized, authorized JSON array; it is not a live TSETMC/Codal parser. No external package, model, or paid service is required.

Each entry requires string instrument_id, symbol and name; aliases is an optional array of strings. IDs are scoped to source_id, not merged by ticker. Original strings and raw input snapshots are preserved. The observation timestamp must include a timezone and is normalized to UTC. It is supplied by the importer, not independently verified.

## Synthetic local demonstration

Create a temporary fixture (not real market data):

```json
[{"instrument_id":"00123","symbol":"نمونه یک","name":"شرکت آزمایشی","aliases":["نمونه۱"]}]
```

```sh
python -m v4invest.catalog --db data/demo.sqlite3 import-json fixture.json --source synthetic --url https://example.org/synthetic --observed-at 2026-01-01T12:00:00+03:30
python -m v4invest.catalog --db data/demo.sqlite3 search 'نمونه یک'
python -m v4invest.catalog --db data/demo.sqlite3 search 'نمونه یک' --as-of 2026-01-01T12:00:00+03:30
python -m unittest discover -s tests -v
```

Results include source, evidence URL, observation timestamp, snapshot ID and same-time conflict flag. Exact symbol matches rank first. Search is a small-catalog lexical baseline, not FTS5 or semantic search. It selects latest observed versions as of the requested time; it does not certify publication time, completeness, current trading status, or independent cross-source identity. No arbitrary network fetching occurs. Imports must be authorized and must not contain credentials or restricted data. Raw snapshots can remain if a later catalog transaction fails; this preserves evidence, not a certified successful import.

## Verification

Local Python 3.13.5: existing 9 tests passed, new tests initially failed because the module did not exist, then full suite passed 17/17. A temporary CLI fixture import and search also passed. The tested catalog, tests and unchanged foundation Python files were compared to GitHub blob SHAs. No live source test: the local execution environment could not resolve github.com; provider permission and live schemas remain unverified. No provider is enabled.

Remaining #1 gates: source terms and security review, exact versions, authorized live schema samples, instrument/price/filing contracts with reconciliation and freshness, cross-source identity mapping and production search scale. Do not merge this partial result as a claim that #1 is complete.
