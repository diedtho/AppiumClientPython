import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def test_selenium_server_available():
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    session.get("http://localhost:4723/wd/hub")
    return session.headers

headers = test_selenium_server_available()
print(headers)