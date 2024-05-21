#!/usr/bin/python3

"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alx api project by Mditau"
    }
    response = requests.get(url , headers=headers, allow_redirects=False)
    if response.status_code == 404:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    else:
        return 0
   