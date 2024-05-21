#!/usr/bin/python3

"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alx api project by Mditau"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        # Return 0 for invalid subreddits or other error responses
        return 0
    except requests.RequestException:
        # Return 0 if there is any request exception (network issues, invalid JSON, etc.)
        return 0