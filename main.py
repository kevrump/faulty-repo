from utils import fetch_data

def main():
    response = fetch_data("https://example.com/api/1234")  # Correct: Supply a string with a valid URL
    print(response)

if __name__ == "__main__":
    main()