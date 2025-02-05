```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    return requests.get(url)

def main():
    url = "https://example.com"  # Corrected: give fetch_data a valid URL
    response = fetch_data(url)
    print(response.content)

if __name__ == "__main__":
    main()
```