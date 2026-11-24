# drowsy-limiter-63

[![bounty](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/nuraliana/drowsy-limiter-63/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/nuraliana/drowsy-limiter-63/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

An entry for the make.fun bounty "The Postmortem That Made Us Laugh". It tells the story of a coding agent asked to add rate limiting, which dutifully throttled the one endpoint that must never be throttled — the health check. The load balancer, seeing no healthy instances, did exactly what it was built to do and removed them all, one by one, right on schedule. Two sentences, one very bad day.
The joke lands because every step followed the instructions perfectly — the agent did its job, the balancer did its job, and the service still went dark.
It is 175 characters long, short enough to read aloud at a standup and still get the groan.

## Run it

```sh
python3 main.py
```

The program writes the entry text to `entry.txt` inside the directory named by `MAKEFUN_OUTPUT_DIR` (or `/output` when that variable is not set). It checks the entry first: plain text, between 1 and 400 characters, one or two sentences. Standard library only, nothing to install.

Built for [make.fun](https://make.fun/?ref=ctnjhg8e&utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).
