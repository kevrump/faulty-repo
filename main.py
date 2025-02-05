from utils import fetch_data

def main():
    response = fetch_data("https://example.com/data/1234")  # Pass a valid string URL
    print(response)

if __name__ == "__main__":
    main()