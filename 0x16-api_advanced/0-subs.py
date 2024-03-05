import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
    - subreddit: Name of the subreddit
    
    Returns:
    - Number of subscribers (int)
    - If the subreddit is invalid or not found, returns 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User-Agent'}  # Set a custom User-Agent
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0  # If not a valid subreddit, return 0
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return 0
