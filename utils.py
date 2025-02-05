```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    if not isinstance(url, str):
        raise ValueError("URL must be a string")
    return requests.get(url)

def main():
    response = fetch_data("https://example.com")  # ✅ Correct: fetch_data() expects a string
    print(response.text)

if __name__ == "__main__":
    main()
```