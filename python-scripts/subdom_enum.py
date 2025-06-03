import requests
import sys


def subdom_enum(domain):

    sub_list = open("common_subdomain.txt").read()
    subdoms = sub_list.splitlines()

    for sub in subdoms:
        sub_domains = f"http://{sub}.{domain}"

        try:
            requests.get(sub_domains)

        except requests.ConnectionError:
            pass

        else:
            print("Valid domain: ", sub_domains)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 subdom_enum.py <domain> <file_name>")
        sys.exit(1)

    target_domain = sys.argv[1]
    
    subdom_enum(target_domain)
    
