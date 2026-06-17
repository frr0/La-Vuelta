# La-Vuelta

La-Vuelta is a small Telegram bot for following the race standings for team-based fantasy tracking. It reads local rider lists, calculates points, and exposes the results through simple bot commands.

## What it does

- Shows the current team lineups.
- Displays the general ranking pulled from La Vuelta data.
- Calculates points for two tracked teams.
- Updates the output files used by the bot workflow.

## Project files

- `bot.py` - main bot script.
- `team1.txt` - riders for team 1.
- `team2.txt` - riders for team 2.
- `ranking.txt` - ranking data consumed by the bot.
- `Points.txt` - accumulated points output.
- `classifica.txt` - additional race classification data.
- `Makefile` - convenience command for generating ranking output.

## Requirements

- Python 3.10 or newer.
- A Telegram bot token.
- Firefox and `geckodriver` for the Selenium portion of the script.
- Python packages used by the project:
	- `python-telegram-bot`
	- `requests`
	- `beautifulsoup4`
	- `selenium`

## Setup

1. Create and activate a virtual environment.
2. Install the dependencies listed above.
3. Configure your Telegram bot token and any local wiring the script expects.
4. Make sure the team files contain the rider names you want to track.

## Run

The repository includes a simple Makefile target that refreshes the ranking output:

```bash
make run
```

If you want to launch the bot directly, run:

```bash
python3 bot.py
```

## Bot commands

- `/start` - shows the welcome message and quick buttons.
- `/team1` - shows team 1 riders and points.
- `/team2` - shows team 2 riders and points.
- `/ranking` - shows the general ranking summary.
- `/help` - lists the available commands.

## Notes

This project is still fairly experimental and some parts are tightly coupled to local files and live race data. If you want, the next good step is to add a `requirements.txt` and a more reliable configuration layer for the token and data sources.
