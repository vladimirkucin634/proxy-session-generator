from proxy_utils import get_proxies
from session_factory import get_session_with_proxy
from config import HEADERS

def main():
    proxies = get_proxies()
    if proxies:
        session = get_session_with_proxy(proxies, HEADERS)
        response = session.get("https://httpbin.org/ip")
        print("Response from httpbin.org/ip:", response.text)
    else:
        print("No proxies available.")

if __name__ == "__main__":
    main()
