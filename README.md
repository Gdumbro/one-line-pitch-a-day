# One-Line Pitch — A Day of One-Line Pitches

Entry for the make.fun bounty `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`.

`main.py` (Python 3.13, standard library only) writes one sentence — a pitch
to convince a friend who has never coded to let an AI agent build their
first app idea on make.fun — to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR` when set, `/output` otherwise).

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The pitch is 150 characters, one sentence, inside the bounty's 1–240
character gate.
