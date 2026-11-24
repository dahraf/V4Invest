"""Local CLI; all network requests require an explicit collect command."""
import argparse
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
from .store import initialize, save_snapshot
from .sources import fetch


def main() -> None:
    parser = argparse.ArgumentParser(description='V4Invest research data foundation')
    parser.add_argument('--db', type=Path, default=Path('data/research.sqlite3'))
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('init')
    sub.add_parser('status')
    collect = sub.add_parser('collect', help='Experimental, read-only public data request')
    collect.add_argument('source', choices=['tsetmc', 'codal'])
    collect.add_argument('--symbol', default='')
    ingest = sub.add_parser('import-json', help='Import a public-data JSON file with provenance')
    ingest.add_argument('file', type=Path)
    ingest.add_argument('--source', required=True)
    ingest.add_argument('--url', required=True)
    ingest.add_argument('--retrieved-at', required=True, help='ISO 8601 including offset; original retrieval time')
    args = parser.parse_args()
    args.db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(args.db) as db:
        initialize(db)
        if args.command == 'collect':
            try:
                url, payload = fetch(args.source, args.symbol)
                print('Snapshot:', save_snapshot(db, args.source, url, payload, datetime.now(timezone.utc).isoformat()))
            except (OSError, ValueError) as exc:
                parser.exit(1, f'Collection failed: {exc}\n')
        elif args.command == 'import-json':
            payload = json.loads(args.file.read_text(encoding='utf-8'))
            print('Snapshot:', save_snapshot(db, args.source, args.url, payload, args.retrieved_at))
        else:
            for table in ('snapshots', 'observations'):
                print(f'{table}: {db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]}')

if __name__ == '__main__':
    main()
