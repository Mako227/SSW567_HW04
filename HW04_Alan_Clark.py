"""
   File Name:    HW04_Alan_Clark.py
   Author:       Alan Clark
   Date:         9 Oct 2021
   Description:  SSW-567 week 5a homework to mock out service calls
"""

import urllib.request
import json
import re
import ssl
import requests

def get_github_commits(user_id : str):
    """ Get and display repository information from GitHub for the user ID entered """
    # Create a context for the service request.
    # I copied this from a textbook without understanding it.
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # With the user ID, create a URL and use it to request the data
    print('\nRetrieving repository data for GitHub user ' + user_id + '\n')
    url1 = 'https://api.github.com/users/' + user_id + '/repos'
    repo_page = urllib.request.urlopen(url1, context=ctx)
    data = repo_page.read().decode()

    # Regex time -- find all lines containing repository names
    result = re.findall('\"name\":[ ]*\"[^"]+\",', data)
    # Extract just the repository names, and use those to count commits
    for raw1 in result:
        if not raw1 == 'None':
            # Strip away everything but the repository name
            raw2 = raw1.replace("\"name\":\"", "")
            repo_name = raw2.replace("\",", "")
            # Build a URL for this repository
            url2 = 'https://api.github.com/repos/' + user_id + '/' + repo_name + '/commits'
            # Use URL to get a requests.Response object for the commits page
            commits_page = requests.get(url2)
            print("Repo: " + repo_name + ", Number of commits: " + str(len(commits_page.json())))
