#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

    If the response body is properly JSON formatted and not empty,
        display the id and name like this: [<id>] <name>
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        q = argv[1]
    except:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        data = r.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except:
        print('Not a valid JSON')
