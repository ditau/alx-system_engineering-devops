import requests

def top_ten(subreddit):
    """Print the titles of the top 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent: alx api project by Mditau "
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if respose_status_code == 404:
        print("None")
        return
    results = response.json().get("data").get("children")
    for post in response:
        print(post.get("data".get("title")))