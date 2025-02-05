```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)

def main():
    response = fetch_data("https://example.com/1234")  # Provide a valid URL as a string
    print(response.content)

if __name__ == "__main__":
    main()
```