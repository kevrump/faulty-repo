from utils import fetch_data

def main():
    response = fetch_data("https://example.com/1234")  # Correct: Pass a valid URL as a string
    print(response)

if __name__ == "__main__":
    main()