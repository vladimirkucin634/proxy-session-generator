# Proxy Session Generator

A Python tool that automatically fetches free HTTP/HTTPS proxies, builds resilient `requests.Session` objects, and applies retry logic for robust web scraping or API interaction.

---

## Proxy Source

Proxies are fetched in real-time from [https://free-proxy-list.net/](https://free-proxy-list.net/), a public site that lists free, updated proxy servers in a tabular format.

---

## Features

- **Automatic proxy list parsing** from an HTML table
- **Retry strategy** using `urllib3.util.retry.Retry` and `HTTPAdapter`
- **Handles common request failures**, such as:
  - Connection errors
  - Read timeouts
  - 4xx/5xx HTTP status codes (`400`, `403`, `429`, `500`, etc.)
- **Proxy selection is random** from the latest proxy list
- **Custom headers support** for realistic browser emulation
- **SSL verification** via `certifi`

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```
