import requests
import time
from concurrent.futures import ThreadPoolExecutor

def running():
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5
    with ThreadPoolExecutor() as executor:
        responses = list(executor.map(lambda url: requests.get(url).json(), urls))
    
    data = range(5000)
    processed_data = list(data)

    large_list_1 = set(range(3000))
    large_list_2 = set(range(2000, 5000))
    common_elements = list(large_list_1 & large_list_2)

    time.sleep(2)

    return {"responses": responses, "common_elements": common_elements}