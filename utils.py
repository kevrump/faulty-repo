```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("URL must start with 'http://' or 'https://'.")
    return requests.get(url)

def main():
    response = fetch_data("http://example.com")
    print(response.text)

if __name__ == "__main__":
    main()
```