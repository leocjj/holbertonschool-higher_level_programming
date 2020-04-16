#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        headers = response.info()
    head = headers.get("X-Request-Id")
    print(head)
