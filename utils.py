```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    if not isinstance(url, str):
        raise ValueError("The URL must be a string.")
    return requests.get(url)

def main():
    url = "https://example.com"  # Correct: Provide a valid URL as a string
    response = fetch_data(url)
    print(response.content)

if __name__ == "__main__":
    main()
```