import os
from pathlib import Path

LINE = (
    "Sometimes I finish your sentences in my head and pretend "
    "your version was the one I was going to say."
)


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
