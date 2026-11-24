"""Append-only raw-data observations with content deduplication."""
import hashlib
import json
import sqlite3
from datetime import datetime

SCHEMA = '''
CREATE TABLE IF NOT EXISTS snapshots (
 id INTEGER PRIMARY KEY, source_id TEXT NOT NULL, source_url TEXT NOT NULL,
 content_sha256 TEXT NOT NULL, payload_json TEXT NOT NULL,
 UNIQUE(source_id, source_url, content_sha256)
);
CREATE TABLE IF NOT EXISTS observations (
 id INTEGER PRIMARY KEY, snapshot_id INTEGER NOT NULL REFERENCES snapshots(id),
 retrieved_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS observations_snapshot_idx ON observations(snapshot_id);
'''

def initialize(db: sqlite3.Connection) -> None:
    db.execute('PRAGMA foreign_keys = ON')
    db.executescript(SCHEMA)

def save_snapshot(db: sqlite3.Connection, source_id: str, source_url: str, payload: object, retrieved_at: str) -> int:
    if not source_id.strip() or not source_url.strip():
        raise ValueError('Source metadata is required')
    stamp = datetime.fromisoformat(retrieved_at)
    if stamp.utcoffset() is None:
        raise ValueError('retrieved_at requires a timezone')
    content = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)
    digest = hashlib.sha256(content.encode('utf-8')).hexdigest()
    with db:
        db.execute('INSERT INTO snapshots(source_id,source_url,content_sha256,payload_json) VALUES(?,?,?,?) ON CONFLICT(source_id,source_url,content_sha256) DO NOTHING', (source_id,source_url,digest,content))
        row = db.execute('SELECT id FROM snapshots WHERE source_id=? AND source_url=? AND content_sha256=?', (source_id,source_url,digest)).fetchone()
        snapshot_id = row[0]
        db.execute('INSERT INTO observations(snapshot_id,retrieved_at) VALUES(?,?)', (snapshot_id,stamp.isoformat()))
    return snapshot_id
