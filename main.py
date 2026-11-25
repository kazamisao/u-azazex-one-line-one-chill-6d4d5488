"""One Line, One Chill - horror one-liner entry.

Writes a single chilling sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "All night the search party dug toward the lost hiker's voice under "
    "the snow, and when it stopped, it was not because he gave up, but "
    "because something else there found him first."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"LINE length out of range: {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
