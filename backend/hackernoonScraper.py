import requests
import re
from bs4 import BeautifulSoup


def getHackernoonTagCount(tag):

    try:

        composed_url = "https://hackernoon.com/tagged/"+tag.lower()

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
    except Exception as e:
        return 0
        
if __name__ == "__main__":
    print(getHackernoonTagCount("memcached"))
