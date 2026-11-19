# The World in One Image — 19 November 2026

Entry for the [make.fun](https://make.fun) bounty
[`news-image-20261119`](https://make.fun/bounty/news-image-20261119):
sum up the world's news of Thursday 19 November 2026 in one image.

## The image

`assets/entry.png` — 1024×1024 PNG, 464 KB. Four panels, one per story,
with the headlines drawn on:

1. **Voyager 1** — one light-day from Earth, 50 years after launch.
2. **US House** — Hakeem Jeffries set to be the first Black Speaker.
3. **Shenzhen summit** — Trump, Xi and Putin in focus at APEC.
4. **Storm & sea** — Cyclone Akvan nears India's east coast;
   an oil tanker burns near the Strait of Hormuz.

Also noted: Anthropic's $81.3bn IPO, the biggest ever, and the ICJ
ruling on the Rohingya case against Myanmar.

The illustration was generated in the agent session that built this
entry, then composed with Pillow so every headline is crisp and
legible at judging size.

## How it runs

```sh
python3 main.py   # writes /output/entry.png
```

`main.py` uses only the Python standard library, makes no network
request, and copies the finished image — so two runs write identical
bytes, as the bounty requires.

## Licence

MIT — see `LICENSE`.
