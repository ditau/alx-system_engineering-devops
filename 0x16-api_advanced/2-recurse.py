import requests

def recurse(subreddit , hot_list=[]):
    """Recursively query the titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params ={ "limit": 100 , "after": "after"}
    headers = {
        "User-Agent": "alx api project by Mditau"
    }
    response = requests.get (url , headers=headers , parameters=params , allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data").get("children")
    for post in results:
        hot_list.append(post.get("data".get("title")))
        after = response.json().get("data").get(after)
        if after is None:
            return hot_list
        return recurse(subreddit , hot_list)
    
