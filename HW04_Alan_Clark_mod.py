"""
   File Name:    HW04_Alan_Clark_mod.py
   Author:       Alan Clark
   Date:         9 Oct 2021
   Description:  Function to return number of commits to a GitHub repository
"""

import json
import requests

def get_github_commits(user_id : str, repo_id : str) -> int:
    """ Get and display number of commits for the entered user and repository """

    # Create the URL
    url_1 = 'https://api.github.com/repos/' + user_id + '/' + repo_id + '/commits'
    # Use it to get a requests.Response object for the commits page
    commits_page = requests.get(url_1)
    # Return the number of commits
    return len(commits_page.json())

# Quick test
#print('Repo: SSW567_HW02, Number of commits: ' + str(get_github_commits('Mako227', 'SSW567_HW02')))
