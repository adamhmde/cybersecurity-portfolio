import requests
import sys

def enumerate_urls(domain, subdomain_list, path_list):
    with open(subdomain_list, "r") as f:
        subdomains = f.read().splitlines()

    with open(path_list, "r") as f:
        paths = f.read().splitlines()

    for sub in subdomains:
        for path in paths:
            url = f"https://{sub}.{domain}/{path}"
            try:
                response = requests.get(url, timeout=3, headers={"User-Agent": "Mozilla/5.0"})
                if response.status_code < 400:
                    print(f"[+] Found: {url} (Status: {response.status_code})")
            except requests.RequestException:
                pass  # Ignore failed requests

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 subdom_enum.py <domain> <subdomain_wordlist> <path_wordlist>")
        sys.exit(1)

    target_domain = sys.argv[1]
    sub_wordlist = sys.argv[2]
    path_wordlist = sys.argv[3]

    enumerate_urls(target_domain, sub_wordlist, path_wordlist)