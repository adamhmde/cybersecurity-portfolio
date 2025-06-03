import requests
import sys


def directory_enum():

    sub_list = open("common_dir_subdom.txt").read()
    directories = sub_list.splitlines()

    for dir in directories:
        dir_enum = f"http://{target_url}/{dir}.html"
        r = requests.get(dir_enum)
        if r.status_code == 404:
            pass
        else:
            print("Valid directory:", dir_enum)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 directory_enum.py <target_url>")
        sys.exit(1)

    target_url = sys.argv[1]
