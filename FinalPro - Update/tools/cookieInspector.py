import requests

def get_cookies_from_url():
    url = input("Enter the URL: ")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.cookies:
            for cookie in response.cookies:
                print("Cookie:", cookie.name)
                print("Value:", cookie.value)
        else:
            print("No cookies found for this URL.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_cookies_from_url()
