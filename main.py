from utils import fetch_data

def main():
    response = fetch_data("https://example.com")  # Changed to a valid URL string
    print(response)

if __name__ == "__main__":
    main()