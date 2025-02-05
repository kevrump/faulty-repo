from utils import fetch_data

def main():
    response = fetch_data("https://example.com/path/to/resource")  # Provide a valid URL as a string
    print(response)

if __name__ == "__main__":
    main()