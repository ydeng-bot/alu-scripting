# alu-scripting

## Regular Expressions

This directory contains Ruby scripts that build and apply regular expressions to solve a variety of pattern-matching problems, from simple literal matches to parsing real-world log data.

### Description

Regular expressions (regex) are patterns used to match character combinations in strings. This project explores Ruby's regex engine (built on the Oniguruma library) through a series of small, focused scripts — each one accepts a single command-line argument, applies a regex to it, and prints the result.

### Requirements

- All scripts are written in Ruby and tested on Ubuntu 20.04 LTS
- The first line of every script is `#!/usr/bin/env ruby`
- All scripts are executable (`chmod +x`)
- All files end with a new line
- All regexes are built for the Oniguruma library (Ruby's native regex engine)

### Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-simply_match_school.rb` | Matches and extracts every occurrence of the literal string `School` in the input |
| 1 | `1-repetition_token_0.rb` | Matches a set of given cases using a repetition token |
| 2 | `2-repetition_token_1.rb` | Matches a set of given cases using a repetition token |
| 3 | `3-repetition_token_2.rb` | Matches a set of given cases using a repetition token |
| 4 | `4-repetition_token_3.rb` | Matches a set of given cases using a repetition token (no square brackets allowed) |
| 5 | `5-beginning_and_end.rb` | Matches a string that starts with `h`, ends with `n`, with exactly one character in between |
| 6 | `6-phone_number.rb` | Matches a valid 10-digit phone number with no spaces, dashes, or extra characters |
| 7 | `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts every capital letter from the input string |
| 8 | `8-textme.rb` | Parses a TextMe log line and outputs `SENDER,RECEIVER,FLAGS` |
| 9 | `9-passed_linkedin_regex_challenge.jpg` | Screenshot proof of completing LinkedIn's regex puzzle |

### Usage

Each script is run from the command line with a single argument:

```bash
./0-simply_match_school.rb "Best School"
```

### Author

This project is part of the ALX Software Engineering program, System Engineering & DevOps track.
