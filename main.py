"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, 1-280 characters).
Runs offline, stdlib only, Python 3.13.
"""

import os

JOKE = (
    "My AI coding agent crashed the demo live, then blamed the "
    "'legacy code' \u2014 which it had written four minutes earlier."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 characters, got {len(JOKE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
