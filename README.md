# The World in One Day — 26 November 2026

[![make.fun](https://make.fun/badge.svg)]()

A single-image infographic summing up Thursday 26 November 2026's
world news: six of the day's biggest stories, from the deadly fuel
tanker fire outside Cairo to Wall Street's AI-driven slide, Russia's
war toll, Pakistan's first astronaut reaching China's Tiangong station,
BepiColombo's arrival at Mercury, and the hostage rescue in Colombia.

## What's inside

- `entry.png` — the 1024x1024 infographic (the submission image)
- `main.py` — copies `entry.png` into the output directory

## Run

```sh
python3 main.py
```

By default the image is copied to `/output/entry.png`. Set
`MAKEFUN_OUTPUT_DIR` to choose another directory:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Stories were checked against major news coverage published on
26 November 2026 (Reuters, AP, BBC and others via their reporting of
the day's events).

## License

MIT — see `LICENSE`.
