from utils import fetch_data

def main():
    response = fetch_data("https://example.com/1234")  # Pass a valid URL string
    print(response)

if __name__ == "__main__":
    main()