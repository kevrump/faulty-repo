def running():
    import concurrent.futures

    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 5
    responses = []

    def fetch_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    with concurrent.futures.ThreadPoolExecutor() as executor:
        fetched_responses = executor.map(fetch_url, urls)

    responses = [response for response in fetched_responses if response is not None]

    processed_data = list(range(5000))

    large_list_1 = set(range(3000))
    large_list_2 = set(range(2000, 5000))
    common_elements = list(large_list_1 & large_list_2)

    time.sleep(2)

    return {"responses": responses, "common_elements": common_elements}