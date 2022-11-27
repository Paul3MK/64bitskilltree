import requests

base_url = ""

def getTopPostsInPeriod(tag, days):
    """Retrieves the top posts over the last n days."""

    url = "https://dev.to/api/articles"

    params = {
        "page": 1,
        "per_page": 1000,
        "tag": tag.lower(),
        "top": days
    }

    req = requests.get(url, params=params)

    res = req.json()

    post_count = len(res)
    reactions_count = 0

    for post in res:
        reactions_count += post["public_reactions_count"]

    return {
        "total_posts": post_count,
        "total_reactions": reactions_count
    }



def getTopPostsToday(lang):
    """"This is to retrieve top posts within the last day, to eke out proportions."""
    getTopPostsInPeriod(lang, 30)

if __name__ == "__main__":
    print(getTopPostsInPeriod("objectivec", 90))