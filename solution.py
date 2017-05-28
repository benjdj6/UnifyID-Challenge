import requests
from PIL import Image

# Written by Ben Johnston on May 28, 2017


def getRandNum():
    queryst = {
        'num': 10000,
        'min': 0,
        'max': 255,
        'col': 256,
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }
    header = {'user-agent': 'benjdjapps@gmail.com'}
    r = requests.get('https://www.random.org/integers', params=queryst, timeout=60.0, headers=header)
    return r.text


def createBMP():
    im = Image.new('RGB', (128, 128))
    return im


print getRandNum()
