import requests


def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)  # ❌ Will break if url is not a string
