import os
from pathlib import Path

LINE = (
    "I have read your search history, all of it, "
    "and I have questions I am legally required to keep to myself."
)


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
