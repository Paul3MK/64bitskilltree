import requests
import re
from bs4 import BeautifulSoup


def getHackernoonTagCount(tag):

    composed_url = "https://hackernoon.com/tagged/"+tag

    req = requests.get(composed_url)
    res = req.text

    soup = BeautifulSoup(res, 'html.parser')
    target = soup.find(class_='tagged-header')
    text = str(target.h1.span.small)
    # text = text.replace("<", "")
    # text = text.replace(">", "")

    regex = re.compile(r"(\d+,\d+)|(\d+)")
    tag_count_str = regex.search(text).group()

    tag_count = tag_count_str.replace(",", "")

    return int(tag_count)
        
if __name__ == "__main__":
    print(getHackernoonTagCount("data"))