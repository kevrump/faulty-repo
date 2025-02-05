```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)

def main():
    response = fetch_data("https://example.com")  # Correct: fetch_data() expects a string
    print(response.content)

if __name__ == "__main__":
    main()
```