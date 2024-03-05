#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404 or "data" not in response.json():
            return 0
        results = response.json()["data"]
        return results.get("subscribers", 0)  # Return 0 if 'subscribers' key is not present
    except requests.RequestException:
        return 0

