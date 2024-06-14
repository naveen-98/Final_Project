import urllib.request
from urllib.error import HTTPError, URLError

def fetch_web_page(url):
    # Ensure the URL has a scheme
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    # Create a request object with a User-Agent header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = urllib.request.Request(url, headers=headers)

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode("utf-8")
            print(html_content)

    # Handle HTTP errors
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")

    # Handle URL errors (e.g., malformed URL)
    except URLError as e:
        print(f"URL Error: {e.reason}")

    # Handle all other exceptions
    except Exception as ex:
        print(f"Exception: {ex}")

if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    fetch_web_page(url)
