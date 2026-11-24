"""Experimental read-only public-data adapters. Live availability is not certified."""
import json
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler

MAX_BYTES = 32 * 1024 * 1024

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def endpoint(source: str, symbol: str = '') -> tuple[str, str]:
    if source == 'tsetmc':
        params = {'market': 0, **{f'paperTypes[{i}]': i + 1 for i in range(9)}, 'withBestLimits': 'false', 'hEven': 0, 'RefID': 0}
        return 'https://cdn.tsetmc.com/api/ClosingPrice/GetMarketWatch?' + urlencode(params), 'marketwatch'
    if source == 'codal':
        if not symbol.strip():
            raise ValueError('Codal requires --symbol')
        params = {'Audited': 'true', 'AuditorRef': -1, 'Category': -1, 'Childs': 'false', 'CompanyState': 0, 'CompanyType': -1, 'Consolidatable': 'true', 'IsNotAudited': 'false', 'Isic': -1, 'Length': -1, 'LetterType': -1, 'Mains': 'true', 'NotAudited': 'true', 'NotConsolidatable': 'true', 'PageNumber': 1, 'Publisher': 'false', 'Symbol': symbol.strip(), 'TracingNo': -1, 'search': 'true'}
        return 'https://search.codal.ir/api/search/v2/q?' + urlencode(params), 'Letters'
    raise ValueError('Unknown provider')


def parse_response(body: bytes, expected_key: str) -> dict:
    try:
        result = json.loads(body)
    except (ValueError, UnicodeError) as exc:
        raise ValueError('Invalid JSON response') from exc
    if not isinstance(result, dict) or not isinstance(result.get(expected_key), list):
        raise ValueError(f'Unexpected response schema: {expected_key}')
    return result


def fetch(source: str, symbol: str = '') -> tuple[str, dict]:
    url, key = endpoint(source, symbol)
    request = Request(url, headers={'Accept': 'application/json', 'User-Agent': 'V4Invest/0.1 (research; read-only)'})
    with build_opener(NoRedirect()).open(request, timeout=20) as response:
        body = response.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError('Response exceeds size limit')
    result = parse_response(body, key)
    if not result[key]:
        raise ValueError('Empty response; cannot certify fresh data')
    return url, result
