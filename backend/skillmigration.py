import twitterAPICaller as tw
import githubAPICaller as gh
import pypl
import stackoverflow as so
import himalayasAPICaller as hm
import remotiveAPICaller as rm
import hackernoonScraper as ha
import devtoAPICaller as dv
import skills

import pymongo
from dotenv import load_dotenv
from os import environ as env
import asyncio

himalayas_jobs = hm.jobGetter("offline")
himalayas_results = hm.jobChecker(himalayas_jobs)
himalayas_skill_count = hm.skilledJobCount(himalayas_results)

remotive_jobs = rm.remotiveJobGetter("offline")
remotive_results = rm.remotiveJobChecker(remotive_jobs)
remotive_skill_count = rm.skilledJobCount(remotive_results)


def loadLang(lang):
    # get website
    # get docs
    # get roadmap.sh
    # get Awesome
    lang_info = skills.skillInfo(lang)
    
    
    # get twitter data
    tweetcount = tw.getAllTweetCounts(lang)
    # get GitHub data
    repo_count = asyncio.run(gh.getRepositories(lang))
    issue_count = asyncio.run(gh.getIssues(lang))
    # get PyPL data
    pypl_data = pypl.pypl(lang)
    # get SO info
    so_twoyears = so.GetTwoYearCount(lang)
    so_day = so.Get24HourCount(lang)
    so_week = so.GetWeekStats(lang)
    # get Himalayas ads


    himalayas_lang = himalayas_skill_count[lang]
    # get Remotive ads

    remotive_lang = remotive_skill_count[lang]
    # get Hackernoon article count
    hackernoon_count = ha.getHackernoonTagCount(lang)
    # get dev.to article count (90d)
    devto_count = dv.getTopPostsInPeriod(lang, 90)
    # get latest hackernoon articles
    # get latest dev.to articles

    # set type: language

    load_dotenv()
    client = pymongo.MongoClient(env['LOCAL_MONGO_URI'])
    db = client.sixtyfour2
    
    language = {
        "type": lang_info["type"],
        "language": lang_info["language"],
        "site": lang_info["site"],
        "docs": lang_info["docs"],
        "roadmap": lang_info["roadmap"],
        "awesome": lang_info["awesome"],
        "himalayas_open_jobs": himalayas_lang,
        "remotive_open_jobs": remotive_lang,
        "hackernoon_posts": hackernoon_count,
        "devto_post": devto_count,
        "twitter": {
            "count": tweetcount["meta"]["total_tweet_count"],
            "data": tweetcount
        },
        "github": {
            "repos": repo_count,
            "issues": issue_count
        },
        "pypl": pypl_data,
        "stackoverflow":{
            "two_year": so_twoyears,
            "today": so_day,
            "week": so_week
        }

    }

    collection = db.lang
    collection.insert_one(language)

def updateLang(lang):    
    pass

if __name__ == "__main__":
    # loadLang("JavaScript")
    loadLang("Python")
    loadLang("Java")
    loadLang("Go")