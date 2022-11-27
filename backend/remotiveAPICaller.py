import requests as re
import datetime
from trie import TrieNode
import skills
import json

d = {}

skill_dict = skills.fullList(d)
skill_count = {}
for i in skill_dict:
    skill_count[i] = 0


def remotiveJobGetter(state):

    if state == "offline":
        with open("rem.json", "r") as f:
            site_dump = json.load(f)
    elif state == "online":
        job = re.get("https://remotive.com/api/remote-jobs")
        site_dump = job.json()
    else:
        return

    # job_directory = []


    # for j in site_dump["jobs"]:

    #     job_directory.append(
    #         {
    #             "job-title": j["title"],
    #             "employer": j["company_name"],
    #             "description": j["description"],
    #             "published-on": datetime.datetime.fromisoformat(j["publication_date"]).strftime("%c"),
    #             "link": j["url"]
    #         }
    #     )

    # return job_directory

    return site_dump["jobs"]

def remotiveJobChecker(job_array):
    """Returns a dict of the total count of skill occurrences in remotive jobs"""
    result_set = []

    t = TrieNode()

    for skill in skill_dict:
        t.addPhrase(t, skill_dict[skill], skill)

    for job in job_array:
        t.findPhrases(t, job["description"], skill_count)
        
    return skill_count

def skilledJobCount(count):
    """Returns a formatted dict of count of skill occurrence"""
    final = {}

    for i in range(1, len(skill_dict)):
        final[skill_dict[i]] = count[i]


    return final

# def getSkillJobs(skill, final_dict):
    
#     return final_dict[skill]

if __name__ == "__main__":
    # job_list = remotiveJobGetter()
    # print(job_list)
    with open("rem.json", "r") as f:
        job_list = json.load(f)["jobs"]
        print(remotiveJobChecker(job_list))