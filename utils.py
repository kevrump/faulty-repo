```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    return requests.get(url)

def main():
    response = fetch_data("https://example.com")  # Use a valid URL string
    print(response.text)
    
if __name__ == "__main__":
    main()
```