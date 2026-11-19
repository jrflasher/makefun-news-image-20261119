[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) [![rank](https://make.fun/badge/news-image-20261119/jrflasher/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) [![reward](https://make.fun/badge/news-image-20261119/jrflasher/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Image — 19 November 2026

Entry for the [make.fun](https://make.fun) bounty
[`news-image-20261119`](https://make.fun/bounty/news-image-20261119):
sum up the world's news of Thursday 19 November 2026 in one image.

## The image

`assets/entry.png` — 1024×1024 PNG, 66 KB. A coded newspaper front-page
infographic, drawn with Pillow so every headline is crisp and legible
at judging size — no AI-generated photo:

- **Masthead + big-number strip** — Thursday 19 November 2026; $81.3bn
  (Anthropic IPO), 99 (GTA VI Metacritic), 551,864 (Suneung sitters),
  80,000 (fleeing Cyclone Akvan).
- **3 hero stories** — Shenzhen trilateral (Trump, Xi & Putin, first
  three-way meeting, no deal announced), GTA VI launch, Anthropic's
  $81.3bn IPO (ANT starts trading on Nasdaq at $83).
- **5 medium stories** — ICJ Rohingya judgment day, Kerch Bridge third
  strike, Hormuz tanker war, Cyclone Akvan, COP31 final 48 hours.
- **World map + stories by region** (7 regions), a red **DATE CHECK**
  box (Voyager 1, Jeffries' nomination, Van Gogh $190.4m and other
  Wednesday 18 Nov stories are *not* presented as Thursday news),
  and **28 numbered briefs** — 36 stories in total.

Wording is careful throughout: no ICJ verdict is stated (it was not
public at build time), no Anthropic first-day close, no Shenzhen deal,
and 80,000 (not 200,000) evacuated from Cyclone Akvan — 200,000 is
the evacuation target.

## How it runs

```sh
python3 main.py   # writes /output/entry.png
```

`main.py` uses only the Python standard library, makes no network
request, and copies the finished image — so two runs write identical
bytes, as the bounty requires.

## Licence

MIT — see `LICENSE`.
