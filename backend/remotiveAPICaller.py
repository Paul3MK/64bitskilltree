import requests as re
import datetime
from trie import TrieNode

skill_dict = {1: "Python", 2: "Vertex", 3: "java", 4: "AWS"}

def remotiveJobGetter():
    job = re.get("https://remotive.com/api/remote-jobs?category=software-dev&limit=5")

    site_dump = job.json()

    job_directory = []


    for j in site_dump["jobs"]:

        job_directory.append(
            {
                "job-title": j["title"],
                "employer": j["company_name"],
                "description": j["description"],
                "published-on": datetime.datetime.fromisoformat(j["publication_date"]).strftime("%c"),
                "link": j["url"]
            }
        )

    return job_directory

def remotiveJobChecker(job_array):

    result_set = []

    t = TrieNode()

    for skill in skill_dict:
        t.addPhrase(t, skill_dict[skill], skill)

    for job in job_array:
        result_set.append(t.findPhrases(t, job["description"]))
        
    return result_set

job_list = remotiveJobGetter()
print(job_list)
print(remotiveJobChecker(job_list))