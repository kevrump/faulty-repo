from utils import fetch_data

def main():
    response = fetch_data("https://example.com/1234")  # Correct: fetch_data() expects a URL string
    print(response)

if __name__ == "__main__":
    main()