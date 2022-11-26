import requests
import asyncio
import aiohttp
from dotenv import load_dotenv
from os import environ as env
import datetime as dt
import urllib.parse

base_url = "https://api.github.com/search/"

async def getRepositories(lang, base_url="https://api.github.com/search/"):

    load_dotenv()

    now = dt.datetime.now(dt.timezone.utc)
    month_ago = now - dt.timedelta(days=30)
    
    today = now.strftime("%Y-%m-%d")
    last_month = month_ago.strftime("%Y-%m-%d")

    params={
        "q":"stars:>0 pushed:>{} language:{}".format(last_month, lang),
        "per_page":1
    }

    headers={"Authorization": "Bearer "+env['GITHUB_TOKEN']}

    async with aiohttp.ClientSession() as session:

        repos = await session.get(base_url+"repositories", params=params, headers=headers)

        response = await repos.json()

        return response["total_count"]

async def getIssues(lang, base_url="https://api.github.com/search/"):
    load_dotenv()

    now = dt.datetime.now(dt.timezone.utc)
    month_ago = now - dt.timedelta(days=30)
    
    today = now.strftime("%Y-%m-%d")
    last_month = month_ago.strftime("%Y-%m-%d")

    params={
        "q":"comments:>5 updated:>{} language:{}".format(last_month, lang),
        "per_page":1
    }

    headers={"Authorization": "Bearer "+env['GITHUB_TOKEN']}

    async with aiohttp.ClientSession() as session:

        repos = await session.get(base_url+"issues", params=params, headers=headers)

        response = await repos.json()

        return response["total_count"]


if __name__ == "__main__":
    pass