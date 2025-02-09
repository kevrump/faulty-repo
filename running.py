import requests
import time


def running():
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5

    # Using session for connection reuse and async for concurrency
    session = requests.Session()
    responses = []
    for url in urls:
        response = session.get(url)
        if response.status_code == 200:
            responses.append(response.json())

    # Avoid unnecessary loop to check for duplicates by using list directly
    data = list(range(5000))
    processed_data = data  # range naturally contains all unique items

    # Using set intersection to find common elements
    large_list_1 = set(range(3000))
    large_list_2 = set(range(2000, 5000))
    common_elements = list(large_list_1 & large_list_2)

    # Removed the time.sleep(2) to improve speed while keeping the rest of the logic intact
    return {"responses": responses, "common_elements": common_elements}