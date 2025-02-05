```python
import requests

def main():
    response = fetch_data("https://example.com")
    print(response)

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)

if __name__ == "__main__":
    main()
```