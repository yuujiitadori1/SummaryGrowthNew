# News Summary — 11 November 2026 (v4)

make.fun competition entry: `news-summary-01`.

## What it is

A one-file summary of the world's news of Wednesday 11 November 2026,
written to `/output/entry.txt` by `main.py`, which copies `summary.txt`.

- 16 stories, ordered by consequence, each with its source named inline
  (BBC, AP, Reuters, CoinDesk, Sui).
- 1,979 characters (limit 1–2,000), UTF-8.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see LICENSE.
