"""Offline catalog baseline; imports normalized, authorized observations only."""
import argparse
import json
import sqlite3
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from .store import initialize, save_snapshot

SCHEMA = '''
CREATE TABLE IF NOT EXISTS catalog_observations (
    source_id TEXT NOT NULL,
    instrument_id TEXT NOT NULL,
    observed_at TEXT NOT NULL,
    snapshot_id INTEGER NOT NULL REFERENCES snapshots(id),
    record_json TEXT NOT NULL,
    PRIMARY KEY (source_id, instrument_id, observed_at, record_json)
);
CREATE INDEX IF NOT EXISTS catalog_time_idx
    ON catalog_observations(source_id, instrument_id, observed_at DESC);
'''
_TRANSLATION = str.maketrans('يىك۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', 'ییک01234567890123456789')


def normalize(text: str) -> str:
    text = unicodedata.normalize('NFKC', text).translate(_TRANSLATION).casefold()
    return ' '.join(''.join(' ' if ch in '\u200c\u200d' else ch
                            for ch in text if unicodedata.category(ch) != 'Mn').split())


def utc_stamp(value: str) -> str:
    stamp = datetime.fromisoformat(value)
    if stamp.utcoffset() is None:
        raise ValueError('Timezone is required')
    return stamp.astimezone(timezone.utc).isoformat()


def initialize_catalog(db: sqlite3.Connection) -> None:
    initialize(db)
    db.executescript(SCHEMA)


def _record(row: dict) -> dict:
    if not isinstance(row, dict):
        raise ValueError('Instrument must be an object')
    fields = ('instrument_id', 'symbol', 'name')
    if any(not isinstance(row.get(key), str) or not row[key].strip() for key in fields):
        raise ValueError('Instrument ID, symbol and name must be nonempty strings')
    if row['instrument_id'] != row['instrument_id'].strip():
        raise ValueError('Instrument ID must not contain surrounding whitespace')
    aliases = row.get('aliases', [])
    if not isinstance(aliases, list) or any(not isinstance(x, str) or not normalize(x) for x in aliases):
        raise ValueError('Aliases must be nonempty strings')
    if not normalize(row['symbol']) or not normalize(row['name']):
        raise ValueError('Empty normalized name or symbol')
    return {**{key: row[key] for key in fields}, 'aliases': sorted(set(aliases))}


def import_catalog(db: sqlite3.Connection, source_id: str, source_url: str,
                   observed_at: str, rows: list[dict]) -> int:
    """Validate the entire batch, then keep raw evidence and normalized versions."""
    if not isinstance(source_id, str) or not source_id.strip() or source_id != source_id.strip():
        raise ValueError('Source ID is required')
    url = urlsplit(source_url)
    if url.scheme != 'https' or not url.hostname or url.username is not None or url.password is not None:
        raise ValueError('Use a credential-free HTTPS evidence URL')
    stamp = utc_stamp(observed_at)
    if not isinstance(rows, list) or not rows:
        raise ValueError('Nonempty instrument array required')
    records = [_record(row) for row in rows]
    encoded = [json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(',', ':')) for row in records]
    snapshot = save_snapshot(db, source_id, source_url, rows, stamp)
    with db:
        db.executemany('''INSERT INTO catalog_observations
            (source_id,instrument_id,observed_at,snapshot_id,record_json) VALUES(?,?,?,?,?)
            ON CONFLICT(source_id,instrument_id,observed_at,record_json) DO NOTHING''',
            [(source_id, row['instrument_id'], stamp, snapshot, content)
             for row, content in zip(records, encoded)])
    return snapshot


def search_catalog(db: sqlite3.Connection, query: str, *, as_of: str | None = None) -> list[dict]:
    """Latest known record per provider identity; retain equally dated conflicts."""
    term = normalize(query)
    if not term:
        raise ValueError('Search term is required')
    stamp = utc_stamp(as_of) if as_of is not None else None
    rows = db.execute('''WITH ranked AS (
        SELECT c.*, DENSE_RANK() OVER (
            PARTITION BY c.source_id,c.instrument_id ORDER BY c.observed_at DESC) AS version_rank
        FROM catalog_observations c WHERE (? IS NULL OR c.observed_at <= ?)
    ), latest AS (
        SELECT *, COUNT(*) OVER (PARTITION BY source_id,instrument_id) AS versions
        FROM ranked WHERE version_rank=1
    ) SELECT l.source_id,l.observed_at,l.record_json,l.versions,s.source_url,l.snapshot_id
      FROM latest l JOIN snapshots s ON s.id=l.snapshot_id''', (stamp, stamp))
    results = []
    compact = term.replace(' ', '')
    for source, observed, record_json, versions, url, snapshot in rows:
        record = json.loads(record_json)
        names = [normalize(record['symbol']), normalize(record['name']), *map(normalize, record['aliases'])]
        if not any(compact in name.replace(' ', '') for name in names):
            continue
        exact_symbol = compact == names[0].replace(' ', '')
        result = {**record, 'source_id': source, 'source_url': url, 'observed_at': observed,
                  'snapshot_id': snapshot, 'conflict': versions > 1}
        results.append((not exact_symbol, source, record['instrument_id'], record_json, result))
    results.sort(key=lambda item: item[:4])
    return [item[-1] for item in results]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('data/research.sqlite3'))
    sub = parser.add_subparsers(dest='command', required=True)
    ingest = sub.add_parser('import-json')
    ingest.add_argument('file', type=Path)
    ingest.add_argument('--source', required=True)
    ingest.add_argument('--url', required=True)
    ingest.add_argument('--observed-at', required=True)
    search = sub.add_parser('search')
    search.add_argument('query')
    search.add_argument('--as-of')
    args = parser.parse_args()
    args.db.parent.mkdir(parents=True, exist_ok=True)
    try:
        with sqlite3.connect(args.db) as db:
            initialize_catalog(db)
            if args.command == 'import-json':
                snapshot = import_catalog(db, args.source, args.url, args.observed_at,
                                          json.loads(args.file.read_text(encoding='utf-8')))
                print('Snapshot:', snapshot)
            else:
                print(json.dumps(search_catalog(db, args.query, as_of=args.as_of), ensure_ascii=False, indent=2))
    except (ValueError, OSError, sqlite3.Error) as exc:
        parser.exit(1, f'Catalog operation failed: {exc}\n')


if __name__ == '__main__':
    main()
