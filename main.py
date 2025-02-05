from utils import fetch_data

def main():
    response = fetch_data("https://example.com/data/1234")  # Corrected: Passed a string URL
    print(response)

if __name__ == "__main__":
    main()