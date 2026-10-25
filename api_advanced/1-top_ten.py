
#!/usr/bin/python3
"""Queries the Reddit API and prints the first 10 hot post titles."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0 (by /u/yomdeng)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post["data"]["title"])

    except (requests.RequestException, ValueError):
        print(None)
