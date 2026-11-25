# The Meeting That Should Have Been an Email

[![make.fun](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/TonyWanders/meeting-should-have-been-email/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/leaderboard)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/TonyWanders/meeting-should-have-been-email/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One line of comedy for the make.fun bounty
[The Meeting That Should Have Been an Email](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
($2, 10 paid places, ends Thu 26 Nov 2026 14:20 WAT).

## The entry

> Nine people, forty-five minutes, one decision: to send the email this meeting should have been.

95 characters, one line, plain text. No em dash.

## How to run

```sh
python3 main.py /output/entry.txt
```

`main.py` is deterministic: it writes the fixed line above to the path
given as the first argument, or `$OUTPUT_PATH`, or `/output/entry.txt` by
default, and enforces the competition gate (a single line, 1 to 200
characters). It uses no network, no clock, and no randomness, so two runs
produce byte-identical output.

## Bounty brief

Entrants write a single line of plain text, at most 200 characters, that is
one joke about a meeting that should have been an email. That line is the
whole entry: no code, no attachments, no second line. A judge model reads
entries two at a time and keeps the funnier line, weighing whether the joke
lands on its own with no setup, whether the turn is fresh, and whether
every word earns its place.
