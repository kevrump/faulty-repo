```python
import requests
import time
from concurrent.futures import ThreadPoolExecutor


def running():
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5
    
    def fetch(url):
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    with ThreadPoolExecutor() as executor:
        responses = list(filter(None, executor.map(fetch, urls)))

    processed_data = list(range(5000))

    large_list_1 = set(range(3000))
    large_list_2 = set(range(2000, 5000))
    common_elements = list(large_list_1.intersection(large_list_2))

    time.sleep(2)

    return {"responses": responses, "common_elements": common_elements}
```