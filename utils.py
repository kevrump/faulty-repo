```python
import requests

def fetch_data(url: str):
    """Fetches data from the given URL."""
    return requests.get(str(url))  # Ensure url is a string
```