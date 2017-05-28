import requests

# Written by Ben Johnston on May 28, 2017


def getRandNum():
    queryst = {'num': 256, 'min': 0, 'max': 256, 'col': 256, 'base': 10, 'format': 'plain', 'rnd': 'new'}
    r = requests.get('https://www.random.org/integers', params=queryst)
    return r.text


print getRandNum()
