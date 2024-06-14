import urllib.request
from urllib.error import HTTPError
import base64

def fetch_authenticated_url(url, username, password):
    try:
        auth_string = f"{username}:{password}"
        encoded_auth_string = base64.b64encode(auth_string.encode()).decode()
        headers = {'Authorization': f'Basic {encoded_auth_string}'}

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode("utf-8")
            print(html_content)
    except HTTPError as e:
        print("HTTP Error:", e)
    except Exception as ex:
        print("Exception:", ex)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    fetch_authenticated_url(url, username, password)
