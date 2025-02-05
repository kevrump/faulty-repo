from utils import fetch_data


def main():
    response = fetch_data('https://example.com/data/1234')  # ✅ Correct: fetch_data() expects a string
    print(response)


if __name__ == "__main__":
    main()