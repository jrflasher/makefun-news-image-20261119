#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261119.

Sums up the world's news of Thursday 19 November 2026 in one image.

The program is deliberately simple and deterministic, as the bounty
allows ("the simplest program copies an image the repository holds"):
it copies the finished 1024x1024 PNG in assets/entry.png to
/output/entry.png, using only the Python standard library and no
network. Running it twice writes the same bytes both times.

The image itself was built in this agent session (see build_entry.py):
a four-panel editorial illustration, with crisp PIL-drawn headlines,
covering the day's biggest stories:

  1. Voyager 1 reaches one light-day from Earth, 50 years after launch.
  2. Hakeem Jeffries set to become the first Black Speaker of the
     US House of Representatives.
  3. Trump, Xi and Putin in focus at the Shenzhen / APEC summit.
  4. Cyclone Akvan nears India's east coast; an oil tanker burns
     near the Strait of Hormuz.
  Also: Anthropic's $81.3bn IPO, the biggest ever, and the ICJ's
  ruling on the Rohingya case against Myanmar.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "assets", "entry.png")
OUTPUT = "/output/entry.png"


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing image: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
