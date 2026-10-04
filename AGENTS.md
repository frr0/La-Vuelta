# Repository Guidelines

## Overview

La-Vuelta is a small Python Telegram bot that retrieves La Vuelta standings,
calculates points for two local fantasy teams, and serves results through bot
commands. The main application is `bot.py`; team and ranking data live in the
root-level text files.

## Project layout

- `bot.py` contains the bot handlers, scraping logic, ranking parsing, and
  point calculation.
- `team1.txt` and `team2.txt` contain one rider name per line.
- `ranking.txt` is the ranking input consumed by the bot.
- `Points.txt` receives accumulated point output when the script runs.
- `Makefile` provides `make run`, which executes the bot and redirects stdout
  to `ranking.txt`.

## Working conventions

- Target Python 3.10+ and preserve the project's existing runtime dependencies:
  `python-telegram-bot`, `requests`, Beautiful Soup, Selenium, Firefox, and
  geckodriver.
- Keep rider names in team files exactly aligned with the names parsed from the
  standings; matching is currently exact string equality.
- Keep changes focused. Do not reformat unrelated code or replace the legacy
  Telegram/Selenium APIs unless the task explicitly includes that migration.
- Use `pathlib` or context-managed file access for new or modified file I/O.
- Treat bot tokens and credentials as secrets. Load them from ignored local
  configuration or environment variables; never commit a real token.

## Validation

- There is no automated test suite or dependency manifest yet.
- For syntax-only validation that avoids network access and launching Firefox,
  run `python3 -m py_compile bot.py`.
- Do not run `make run` or `python3 bot.py` as a routine check: both start the
  bot and can scrape live data; `make run` also overwrites `ranking.txt`.
- When changing parsing or scoring, test against a copy or fixture of ranking
  data and verify both team totals.

## Generated and local data

- Preserve user-maintained team files unless a task specifically requests their
  update.
- Treat `ranking.txt`, `Points.txt`, and `classifica.txt` as runtime data; be
  explicit before intentionally changing their contents.
