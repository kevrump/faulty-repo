from utils import fetch_data

def main():
    response = fetch_data("https://example.com/api/1234")  # Corrected: fetch_data() expects a string with a valid URL
    print(response)

if __name__ == "__main__":
    main()