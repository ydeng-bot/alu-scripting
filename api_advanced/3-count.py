#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the keywords found in hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/ydeng-bot)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        data = response.json().get("data", {})
    except ValueError:
        return
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            if word in counts:
                counts[word] += 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    lowered = [word.lower() for word in word_list]
    totals = {}
    for word, number in counts.items():
        total = number * lowered.count(word)
        if total > 0:
            totals[word] = total
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
