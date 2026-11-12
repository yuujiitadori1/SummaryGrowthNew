"""News Summary entry for make.fun competition news-summary-01.

Reads summary.txt — a summary of Wednesday 11 November 2026 world news,
16 stories ordered by consequence — from this repository and writes it
verbatim to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, deterministic: two runs write byte-identical output.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    summary = (HERE / "summary.txt").read_text(encoding="utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(summary, encoding="utf-8")


if __name__ == "__main__":
    main()
