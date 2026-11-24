import sqlite3
import unittest
from v4invest.catalog import initialize_catalog, import_catalog, search_catalog

URL = 'https://example.org/synthetic'
T1 = '2026-01-01T12:00:00+03:30'
T2 = '2026-01-02T12:00:00+03:30'
ROW = {'instrument_id': '00123', 'symbol': 'نمونه‌يك', 'name': 'شرکت آزمایشی', 'aliases': ['نمونه یک']}

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        initialize_catalog(self.db)

    def tearDown(self):
        self.db.close()

    def ingest(self, rows, time=T1, source='synthetic'):
        return import_catalog(self.db, source, URL, time, rows)

    def test_persian_alias_and_evidence(self):
        self.ingest([ROW])
        result = search_catalog(self.db, 'نمونه یک')[0]
        self.assertEqual(result['instrument_id'], '00123')
        self.assertEqual(result['source_url'], URL)
        self.assertEqual(result['observed_at'], '2026-01-01T08:30:00+00:00')
        self.assertEqual(search_catalog(self.db, 'شركت آزمايشي')[0]['symbol'], ROW['symbol'])

    def test_repeat_is_idempotent(self):
        self.ingest([ROW]); self.ingest([ROW])
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM catalog_observations').fetchone()[0], 1)

    def test_point_in_time_does_not_leak_new_name(self):
        self.ingest([ROW]); self.ingest([{**ROW, 'symbol':'نمونه دو','aliases':[]}], T2)
        self.assertEqual(search_catalog(self.db, 'نمونه یک'), [])
        self.assertEqual(search_catalog(self.db, 'نمونه یک', as_of=T1)[0]['symbol'], ROW['symbol'])

    def test_distinct_source_ids_and_instruments_not_merged(self):
        self.ingest([ROW, {**ROW, 'instrument_id':'00456'}])
        self.ingest([ROW], source='other')
        self.assertEqual(len(search_catalog(self.db, 'نمونه یک')), 3)

    def test_conflicting_same_time_versions_retained(self):
        self.ingest([ROW]); self.ingest([{**ROW,'name':'نام متفاوت'}])
        matches = search_catalog(self.db, 'نمونه یک')
        self.assertEqual(len(matches), 2)
        self.assertTrue(all(x['conflict'] for x in matches))

    def test_invalid_batch_rejected_before_writes(self):
        with self.assertRaises(ValueError): self.ingest([ROW, {**ROW, 'instrument_id': 123}])
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM snapshots').fetchone()[0], 0)

    def test_blank_and_naive_time_rejected(self):
        with self.assertRaises(ValueError): self.ingest([ROW], '2026-01-01T12:00:00')
        with self.assertRaises(ValueError): search_catalog(self.db, '   ')

    def test_literal_sql_metacharacters(self):
        self.ingest([ROW]); self.assertEqual(search_catalog(self.db, '%'), [])
