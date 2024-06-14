# ipAddressAll.py

import socket

def get_ip_addresses(hostname):
    try:
        ip_addresses = socket.getaddrinfo(hostname, None)
        for ip in ip_addresses:
            print("IP address:", ip[4][0])
    except socket.gaierror as e:
        print("Could not find IP addresses for:", hostname)

if __name__ == "__main__":
    hostname = input("Enter the hostname: ")
    get_ip_addresses(hostname)