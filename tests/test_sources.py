import unittest
from urllib.parse import urlsplit, parse_qs
from v4invest.sources import endpoint, parse_response

class SourceTests(unittest.TestCase):
    def test_market_watch_covers_all_nine_paper_types(self):
        url, key = endpoint('tsetmc')
        self.assertEqual(urlsplit(url).hostname, 'cdn.tsetmc.com')
        query = parse_qs(urlsplit(url).query)
        self.assertEqual([query[f'paperTypes[{n}]'][0] for n in range(9)], [str(n) for n in range(1,10)])
        self.assertEqual(key, 'marketwatch')

    def test_codal_symbol_is_encoded(self):
        url, key = endpoint('codal', 'فملی & نمونه')
        self.assertEqual(urlsplit(url).hostname, 'search.codal.ir')
        self.assertEqual(parse_qs(urlsplit(url).query)['Symbol'], ['فملی & نمونه'])
        self.assertEqual(key, 'Letters')

    def test_non_json_or_wrong_structure_fails(self):
        for body in (b'<html>error</html>', b'{"error":true}', b'{"marketwatch":null}', b'{"marketwatch":{}}'):
            with self.subTest(body=body), self.assertRaises(ValueError):
                parse_response(body, 'marketwatch')

    def test_valid_payload_retained_in_full(self):
        data = parse_response(b'{"marketwatch":[{"price":100}],"time":1}', 'marketwatch')
        self.assertEqual(data, {'marketwatch':[{'price':100}], 'time':1})

    def test_unknown_provider_rejected(self):
        with self.assertRaises(ValueError):
            endpoint('unknown')
