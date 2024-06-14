import socket

def findIP_main():
    hostname = input("Enter the hostname: ")
    try:
        ip_address = socket.gethostbyname(hostname)
        print("IP address:", ip_address)
    except socket.error as e:
        print("Could not find IP address for:", hostname)

if __name__ == "__main__":
    findIP_main()

