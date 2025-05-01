import requests
import logging
from bs4 import BeautifulSoup
from typing import List
from config import PROXIES_URL, REQUEST_TIMEOUT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_proxies(proxies_url: str = PROXIES_URL, timeout: int = REQUEST_TIMEOUT) -> List[str]:
    try:
        response = requests.get(proxies_url, timeout=timeout)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table")
        proxies = []

        if table:
            for row in table.find_all("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) >= 2:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    proxies.append(f"{ip}:{port}")

        if not proxies:
            raise ValueError("No proxies found.")

        return proxies

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching proxies: {e}")
        return []
    except Exception as e:
        logger.error(f"Error parsing proxy list: {e}")
        return []