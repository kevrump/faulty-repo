import requests
import time


def running():
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5
    responses = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            responses.append(response.json())

    data = [i for i in range(5000)]
    processed_data = []
    for item in data:
        if item not in processed_data:
            processed_data.append(item)

    large_list_1 = list(range(3000))
    large_list_2 = list(range(2000, 5000))
    common_elements = []
    for item in large_list_1:
        if item in large_list_2:
            common_elements.append(item)

    time.sleep(2)

    return {"responses": responses, "common_elements": common_elements}
