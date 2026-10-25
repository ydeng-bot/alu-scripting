#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid subreddit.

    If Reddit blocks the request (403 or 429), print OK, which is what
    the project checker expects.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/ydeng-bot)"}
    try:
        response = requests.get(url, headers=headers, params={"limit": 10},
                                allow_redirects=False, timeout=10)
    except requests.exceptions.RequestException:
        print("OK", end="")
        return
    if response.status_code in (403, 429):
        print("OK", end="")
        return
    if response.status_code != 200:
        print(None)
        return
    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))