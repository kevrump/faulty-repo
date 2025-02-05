```python
import requests


def fetch_data(url: str):
    """Fetches data from the given URL."""
    if not isinstance(url, str):
        raise ValueError("URL must be a string")
    return requests.get(url)


def main():
    # Provide a valid URL as a string
    response = fetch_data("https://example.com")
    print(response.text)


if __name__ == "__main__":
    main()
```