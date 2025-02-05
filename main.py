from utils import fetch_data

def main():
    response = fetch_data("https://example.com/resource/1234")  # Corrected: fetch_data() expects a string with a schema
    print(response)

if __name__ == "__main__":
    main()