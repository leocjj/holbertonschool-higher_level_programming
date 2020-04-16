#!/usr/bin/python3
"""
script that takes your Github credentials (username and password) and uses
the Github API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    for commit in r.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
