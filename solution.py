import requests
from random import shuffle
from PIL import Image

# Written by Ben Johnston on May 28, 2017

# req_size defines how many random numbers to request
#   9831 is the default to stay within the 10000 per request limit
#   and to even out the load between requests while minimizing data waste
# low_usage limits number of requests when quota is low
req_size = 9831
low_usage = False


# Check data quota of Random.org
def checkQuota():
    header = {'user-agent': 'benjdjapps@gmail.com'}
    url = "https://www.random.org/quota"
    queryst = {
        'format': 'plain'
    }
    r = requests.get(url, params=queryst, timeout=60.0, headers=header)
    return int(r.text)


# Request req_size random numbers from Random.org
def getRandNum():
    queryst = {
        'num': req_size,
        'min': 0,
        'max': 255,
        'col': 1,
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }
    header = {'user-agent': 'benjdjapps@gmail.com'}
    url = "https://www.random.org/integers"
    r = requests.get(url, params=queryst, timeout=60.0, headers=header)
    nums = map(int, ((r.text).encode('utf-8')).split())
    return nums


# Copy random numbers to pixel values
def writePixels(img, pixels):
    pixelMap = img.load()

    for i in range(128):
        for j in range(128):
            r = pixels.pop()
            g = pixels.pop()
            b = pixels.pop()
            pixelMap[i, j] = (r, g, b)

    return img


# Goes into low data usage mode if the quota isn't high enough
# to fulfill 100% true random data. Request size will be set
# to fit within the quota if 9831 numbers cannot be requested
allowance = checkQuota()
if allowance < 100000:
    req_size = allowance / 8
if allowance < 400000:
    low_usage = True

pixels = getRandNum()

# Either request more random numbers or pseudo-randomly
# shuffle current numbers and append them to pixels, depending
# on remaining data quota
while len(pixels) < 49152:
    if low_usage:
        tmp = pixels[:]
        shuffle(tmp)
        pixels.extend(tmp)
    else:
        pixels.extend(getRandNum())

# Create a new Image object
img = Image.new('RGB', (128, 128), "black")

# Write the pixels and save as random.bmp within this directory
writePixels(img, pixels).save("random.bmp")
