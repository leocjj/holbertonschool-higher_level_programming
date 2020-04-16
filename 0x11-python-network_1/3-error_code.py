#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv

    try:
        url = argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read()
        print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
