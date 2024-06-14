
from tools import findIP_main, dos_main, scan_port_main, who_main, display_wifi_passwords, get_instagram_profile_info, get_cookies_from_url, admin_main, get_ip_addresses, fetch_authenticated_url, fetch_web_page



def display_menu():
    print("Select a tool to run:")
    print("1. Tool 1: Scan website")
    print("2. Tool 2: Resolve hostname to IP address")
    print("3. Tool 3: Who is Lookup")
    print("4. Tool 4: Perform DoS attack")
    print("5. Tool 5: Find Wifi Password")
    print("6. Tool 6: Find Instagram Profile")
    print("7. Tool 7: Cookies information")
    print("8. Tool 8: Scan website Admin Page")
    print("9. Tool 9: Find All IP Address")
    print("10. Tool 10: HTTP authentication")
    print("11. Tool 11: Reading Web Page")
    print("12. Exit")

def get_user_choice():
    return input("Enter your choice (1-12): ")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            scan_port_main()
        elif choice == '2':
            findIP_main()
        elif choice == '3':
            who_main()
        elif choice == '4':
            dos_main()
        elif choice == '5':
            display_wifi_passwords()
        elif choice == '6':
            get_instagram_profile_info()
        elif choice == '7':
            get_cookies_from_url()
        elif choice == '8':
            admin_main()
        elif choice == '9':
            hostname = input("Enter the Hostname:")
            get_ip_addresses(hostname)
        elif choice == '10':
            url = input("Enter the URL: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            fetch_authenticated_url(url, username, password)
        elif choice == '11':
            url = input("Enter the URL of the web page: ")
            fetch_web_page(url)
        elif choice == '12':
            break
        else:
            print("Invalid choice. Please try again.")

        back_to_menu = input("Would you like to go back to the menu? (yes/no): ")
        if back_to_menu.lower() != 'yes':
            break

if __name__ == "__main__":
    main()