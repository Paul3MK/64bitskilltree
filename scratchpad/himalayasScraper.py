from bs4 import BeautifulSoup
import requests as re

# on hold. I'll only implement this if it turns out the API has an issue.

# go fetch the website
site = re.get("https://himalayas.app/companies/toggl/jobs/technical-lead")

site_soup = BeautifulSoup(site, "html5lib")


# target several elements, to pull in the job title, company, date posted and body. div.trix-content element

# load the contents into a job posting dict

# run through the dict and place each member.body into the trie

# throw the results into a database of sorts    