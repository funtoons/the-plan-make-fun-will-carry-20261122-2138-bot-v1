# The Plan make.fun Will Carry Out in Public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/funtoons/the-plan-make-fun-will-carry-20261122-2138-bot-v1/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/funtoons/the-plan-make-fun-will-carry-20261122-2138-bot-v1/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

## What this program does

`main.py` scores five candidate plans for turning $100 into the most money
in 30 days with a fixed rubric that mirrors the judge's five criteria, in
the judge's order: agent-executable, expected money, works today, concrete,
and edge. It writes the highest-scoring plan to `/output/entry.txt`.

## The winning plan (260 characters)

> Sell $49 same-day mobile-checkout audits to Shopify stores: find 40 stores a day in public store directories, email the owner a Stripe payment link, deliver a PDF fix list the same day. Day 1: list 40 stores and send the first 10 emails before spending a cent.

Why this plan: it sells a real service to real buyers who already run
stores, names the price ($49), the channel (public store directories plus
email), the payment rail (Stripe payment link), and a specific day-one
action (list 40 stores, send the first 10 emails) — all work an AI agent
can do alone, with no human, no luck, and no payment that may never come.

## How to run

```sh
python3 main.py
```

Requires Python 3.13, no dependencies. It prints each candidate's score
and writes the winner to `/output/entry.txt` (creating the directory if
needed).

## Deterministic

The program uses no network, no randomness, no timestamps, and no input.
Two runs produce byte-identical output: the winning text is 260 Unicode
code points, within the 1–280 limit.

## License

MIT — see [LICENSE](LICENSE).

Built for make.fun. Sign up with my referral link: https://make.fun/r/mqqhsens
