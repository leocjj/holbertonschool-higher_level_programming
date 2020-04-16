#!/usr/bin/python3
"""
script that takes your Github credentials (username and password) and uses
the Github API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    for i in range(10):
        print(r.json()[i].get('sha'), end=': ')
        print(r.json()[i].get('commit').get('author').get('name'))
