```python
import requests

def main():
    response = fetch_data("https://1234")  # Correct: Pass a valid string URL
    print(response.content)

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(url)

if __name__ == "__main__":
    main()
```