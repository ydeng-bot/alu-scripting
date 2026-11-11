#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import os
import requests

USER_AGENT = "linux:alu-scripting:v1.0 (by /u/ydeng-bot)"


def get_token():
    """Return an app-only OAuth token, or None if unavailable."""
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    secret = os.environ.get("REDDIT_CLIENT_SECRET")
    if not client_id or not secret:
        return None
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=(client_id, secret),
        data={"grant_type": "client_credentials"},
        headers={"User-Agent": USER_AGENT},
        timeout=10)
    if response.status_code != 200:
        return None
    return response.json().get("access_token")


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid subreddit."""
    headers = {"User-Agent": USER_AGENT}
    path = "/r/{}/hot".format(subreddit)
    token = get_token()
    if token:
        headers["Authorization"] = "bearer " + token
        url = "https://oauth.reddit.com" + path
    else:
        url = "https://www.reddit.com" + path + ".json"
    response = requests.get(url, headers=headers, params={"limit": 10},
                            allow_redirects=False, timeout=10)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
