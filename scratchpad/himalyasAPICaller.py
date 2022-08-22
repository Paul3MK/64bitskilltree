import requests as re
import datetime
from trie import TrieNode

skill_dict = {1: "Python", 2: "Vertex", 3: "java"}

def jobGetter():
    job = re.get("https://himalayas.app/jobs/api?limit=5")

    site_dump = job.json()

    # site_dump["jobs"][0]["title"]

    job_directory = []


    for j in site_dump["jobs"]:

        job_directory.append(
            {
                "job-title": j["title"],
                "employer": j["companyName"],
                "description": j["description"],
                "published-on": datetime.datetime.fromtimestamp(j["pubDate"]).strftime("%c"),
                "link": j["guid"]
            }
        )

    return job_directory

def jobChecker(job_array):

    result_set = []

    t = TrieNode()

    for skill in skill_dict:
        t.addPhrase(t, skill_dict[skill], skill)

    for job in job_array:
        result_set.append(t.findPhrases(t, job["description"]))
        
    return result_set

# print(jobGetter())
job_list = jobGetter()
print(job_list)
print(jobChecker(job_list))