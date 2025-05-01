import random
import logging
import requests
import certifi
from typing import List, Dict
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_session_with_proxy(proxies: List[str], headers: Dict[str, str]) -> requests.Session:
    if not proxies:
        raise ValueError("Proxy list is empty. Cannot create a session.")

    proxy = random.choice(proxies)
    logger.info(f"Selected proxy: {proxy}")

    session = requests.Session()
    session.proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    session.verify = certifi.where()
    session.headers.update(headers)

    retry_strategy = Retry(
        total=5,
        connect=5,
        read=5,
        redirect=3,
        status=5,
        status_forcelist=[429, 500, 502, 503, 504, 400, 403],
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE"],
        backoff_factor=1,
        raise_on_status=False
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session
