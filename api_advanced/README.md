# alu-scripting / api_advanced

Python scripts that query the Reddit API with the `requests` module.

## Requirements

- Python 3
- `requests` module (`pip install requests`)
- A custom `User-Agent` is set on every request, and redirects are not
  followed, so invalid subreddits are detected.

## Tasks

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the subscriber count, or 0 for an invalid subreddit |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or `None` if invalid |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` recursively returns a list of all hot post titles, or `None` if invalid |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keywords in hot post titles and prints them sorted by count, then alphabetically |

## Usage

```
python3 0-main.py programming
python3 1-main.py programming
python3 2-main.py programming
python3 3-main.py programming 'python java javascript'
```

## Author

Yom Deng Garang ([ydeng-bot](https://github.com/ydeng-bot))
