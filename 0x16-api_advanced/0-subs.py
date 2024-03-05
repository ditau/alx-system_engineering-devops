import requests
from sys import argv

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
    - subreddit: Name of the subreddit
    
    Returns:
    - Number of subscribers (int)
    - If the subreddit is invalid or not found, returns 0
    """
    user_agent = {'User-Agent': 'Ditau'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json().get('data')
        return data.get('subscribers', 0)
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return 0

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py subreddit_name")
    else:
        subreddit_name = argv[1]
        subscribers = number_of_subscribers(subreddit_name)
        print(f"The number of subscribers in r/{subreddit_name}: {subscribers}")
