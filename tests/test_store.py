import sqlite3
import unittest
from v4invest.store import initialize, save_snapshot

class StoreTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        initialize(self.db)

    def tearDown(self):
        self.db.close()

    def test_duplicate_payload_does_not_duplicate_snapshot(self):
        a = save_snapshot(self.db, 'tsetmc', 'https://cdn.tsetmc.com/api/example', {'price': 100}, '2026-11-24T12:00:00+00:00')
        b = save_snapshot(self.db, 'tsetmc', 'https://cdn.tsetmc.com/api/example', {'price': 100}, '2026-11-24T12:00:01+00:00')
        self.assertEqual(a, b)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM snapshots').fetchone()[0], 1)
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM observations').fetchone()[0], 2)

    def test_changed_payload_preserves_history(self):
        for value in (100, 101):
            save_snapshot(self.db, 'codal', 'https://search.codal.ir/example', {'value': value}, '2026-11-24T12:00:00+00:00')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM snapshots').fetchone()[0], 2)

    def test_non_json_number_rejected(self):
        with self.assertRaises(ValueError):
            save_snapshot(self.db, 'codal', 'https://search.codal.ir/example', {'x': float('nan')}, '2026-11-24T12:00:00+00:00')

    def test_missing_timezone_rejected(self):
        with self.assertRaises(ValueError):
            save_snapshot(self.db, 'codal', 'https://search.codal.ir/example', {}, '2026-11-24T12:00:00')
