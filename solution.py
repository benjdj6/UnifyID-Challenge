import requests
import os, sys
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
    url = "https://www.random.org/integers"
    r = requests.get(url, params=queryst, timeout=60.0, headers=header)
    pix = map(int, ((r.text).encode('utf-8')).split())
    return pix


def createBMP():
    img = Image.new('RGB', (128, 128), "black")
    return img


def writePixels(img, pixels):
    pixelMap = img.load()

    for i in range(128):
        for j in range(128):
            r = pixels.pop()
            g = pixels.pop()
            b = pixels.pop()
            pixelMap[i, j] = (r, g, b)

    return img
