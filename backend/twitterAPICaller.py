import requests
from os import environ as env
from dotenv import load_dotenv

def getAllTweetCounts(skill):

    load_dotenv()
    BEARER_TOKEN = env['TWITTER_BEARER_TOKEN']

    excluding = ["-pay ", "-bot ", "-assignment ", "-homework ", "-writer "]

    query = ""

    for term in excluding:
        query += term

    query += skill

    params = {
        "query": query
    }

    headers = {"Authorization": "Bearer "+BEARER_TOKEN}

    tweet_count = requests.get(url="https://api.twitter.com/2/tweets/counts/recent", params=params, headers=headers)
    res = tweet_count.json()

    return res