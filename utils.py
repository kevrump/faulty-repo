```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)

def main():
    url = "https://example.com/data/1234"  # Correct URL format
    response = fetch_data(url)
    print(response.text)

if __name__ == "__main__":
    main()
```