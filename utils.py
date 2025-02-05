```python
import requests

def main():
    response = fetch_data("http://example.com")  # ✅ URL must be a string
    print(response.status_code)

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)

if __name__ == "__main__":
    main()
```