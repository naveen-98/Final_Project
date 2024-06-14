from sys import argv
from threading import Lock, Thread
from requests import get
from requests.exceptions import ConnectionError, MissingSchema
from queue import Queue
from time import sleep
import os

def admin_main():
    def show_usage_and_exit():
        print("""
        Usage:
        -site <url of website> - Website to scan
        --proxy <protocol>-<proxyserverip:port> - Scan using a proxy server
        --t <seconds> - Time delay between scans
        --w <path/of/custom/wordlist> - Use a custom wordlist

        Examples:
        python admin.py -site http://example.com
        python admin.py -site https://example.com --t 1
        python admin.py -site http://example.com example2.com
        python admin.py -site https://example.com --w /custom/wordlist/list.txt
        python admin.py --proxy http-1.2.3.4:8080 -site http://example.com
        """)
        exit()

    # Initialize variables
    proxy_enable = False
    delay = 0
    file_to_open = 'list.txt'
    websites_to_scan = []

    # Process command-line arguments
    try:
        index_site = argv.index('-site') + 1
        websites_to_scan = argv[index_site:]
    except ValueError:
        user_input = input("Enter the website URL to scan: ")
        websites_to_scan = [user_input]

    if '--proxy' in argv:
        try:
            proxy_index = argv.index('--proxy') + 1
            proxy_protocol, proxy_server = argv[proxy_index].split('-')
            proxy_enable = True
            print('Using Proxy - True')
        except (ValueError, IndexError):
            print('Invalid proxy argument format')
            exit()

    if '--t' in argv:
        try:
            t_index = argv.index('--t') + 1
            delay = int(argv[t_index])
        except (ValueError, IndexError):
            print('Invalid delay argument format')
            exit()

    if '--w' in argv:
        try:
            w_index = argv.index('--w') + 1
            file_to_open = argv[w_index]
        except (ValueError, IndexError):
            print('Invalid wordlist argument format')
            exit()

    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Combine the script directory path with the file name
    file_path = os.path.join(script_dir, file_to_open)

    # Check if the file exists before trying to open it
    if not os.path.exists(file_path):
        print(f"Error: '{file_to_open}' not found in the script's directory.")
        exit()

    msg = """
    author: alienwhatever
    credit github.com/bdblackhat for list.txt
    original-source-of-list.txt -  https://github.com/bdblackhat/admin-panel-finder/blob/master/link.txt

    This tool is for educational and testing purposes only
    I am not responsible for what you do with this tool
    """

    print(msg)

    print_lock = Lock()
    q = Queue()

    def scan_website(website):
        while not q.empty():
            worker = q.get()
            try:
                if proxy_enable:
                    r = get('{}{}'.format(website, worker), proxies={proxy_protocol: proxy_server}, allow_redirects=True)
                else:
                    r = get('{}{}'.format(website, worker))

                if r.ok:
                    print('[Status-code - {}] Success: {}'.format(r.status_code, worker))

            except ConnectionError:
                print('Connection Error')

            except MissingSchema:
                print('ERROR: Missing URL Scheme - Please use full URLs (e.g., https://example.com)')
                exit()

            q.task_done()

    # Load URLs from wordlist and scan websites
    for website in websites_to_scan:
        if not website.endswith('/'):
            website += '/'

        with open(file_path, 'r') as f:
            for line in f:
                q.put(line.strip())

        print('Scanning {}...'.format(website))
        while not q.empty():
            t = Thread(target=scan_website, args=(website,), daemon=True)
            t.start()
            sleep(delay)

        q.join()
        print('\n')

if __name__ == "__main__":
    admin_main()
