import whois

def query_whois(domain):
    try:
        whois_data = whois.whois(domain)
        return str(whois_data)
    except Exception as e:
        return str(e)

def who_main():
    domain = input("Enter the domain name: ")
    whois_result = query_whois(domain)
    print(whois_result)

if __name__ == "__main__":
    who_main()
