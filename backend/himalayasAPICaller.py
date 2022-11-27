import requests as re
import datetime
from trie import TrieNode
import json
import time
import skills

d = {}

skill_dict = skills.fullList(d)
skill_count = {}
for i in skill_dict:
    skill_count[i] = 0


def jobGetter(state):

    if state == "offline":
        with open("him.json", "r") as f:
            site_dump = json.load(f)

            return site_dump["jobs"]
    elif state == "online":
        params = {
            "limit": 200,
            "offset" : 0 
        }

        jobs = re.get("https://himalayas.app/jobs/api", params=params)

        initial_dump = jobs.json()

        params["offset"] = 200

        total_jobs = initial_dump["total_count"]

        max_offset = total_jobs - (total_jobs % 200)

        final_limit = total_jobs % 200

        for i in range(2, int(max_offset/200) + 1):
            more_jobs = re.get("https://himalayas.app/jobs/api", params=params)

            params["offset"] = i * params["limit"]

            new_dump = more_jobs.json()

            initial_dump["jobs"].extend(new_dump["jobs"])

        params["limit"] = final_limit
        final_jobs = re.get("https://himalayas.app/jobs/api", params=params)
        final_dump = final_jobs.json()

        initial_dump["jobs"].extend(final_dump["jobs"])


            # f.write(",\n")
            
        # job_directory = []


        # for j in site_dump["jobs"]:

        #     job_directory.append(
        #         {
        #             "job-title": j["title"],
        #             "employer": j["companyName"],
        #             "description": j["description"],
        #             "published-on": datetime.datetime.fromtimestamp(j["pubDate"]).strftime("%c"),
        #             "link": j["guid"]
        #         }
        #     )
            
        if initial_dump["jobs"][-1] == []:
            initial_dump["jobs"].pop()

        with open("him.json", "w") as f:
                json.dump(initial_dump, f, indent=4)

        return initial_dump["jobs"]
    else:
        return

def jobChecker(job_array):
    """Returns a dict of the total count of skill occurrences in himalayas jobs"""
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

if __name__ == "__main__":
    start = time.time()

    with open("him.json", "r") as f:
        job_list = json.load(f)["jobs"]
        skillcount = jobChecker(job_list)

        print(skillcount)

        print(skilledJobCount(skillcount))

    # job_list = jobGetter()
    # print(jobChecker(job_list))


    execution = time.time() - start
    print("Executed in: {}".format(str(execution)))