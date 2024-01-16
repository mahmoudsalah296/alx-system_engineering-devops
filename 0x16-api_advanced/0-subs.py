#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """gets number of subscribers for a subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "User-Agent"},
                            allow_redirects=False)

    if response.status_code >= 300:
        return 0

    data = response.json().get("data")
    return data.get("subscribers")
