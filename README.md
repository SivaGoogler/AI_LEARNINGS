# AI_LEARNINGS

A small automation learning repository organized by framework:

- `Playwright/assignment.py` — YouTube search scraper using Playwright, saves results to `youtube_data/videos.csv`, generates `youtube_data/gallery.html`, and optionally downloads videos via `yt-dlp`.
- `Selenium/assignment.py` — Selenium UI tests against `https://the-internet.herokuapp.com` covering login, checkboxes, dropdown, and dynamic loading.
- `PyAutoGUI/assignment.py` — macOS desktop automation using PyAutoGUI to open Chrome, navigate to YouTube, search, and click a video.

## Repository structure

- `Playwright/`
  - `assignment.py`
- `Selenium/`
  - `assignment.py`
- `PyAutoGUI/`
  - `assignment.py`
- `requirements.txt`
- `README.md`

## Setup

1. Install Python 3.
2. Install required packages:

```bash
python3 -m pip install -r requirements.txt
```

3. Install Playwright browser dependencies:

```bash
python3 -m playwright install
```

## Run the scripts

### Playwright YouTube bot

```bash
python3 Playwright/assignment.py
```

This will:
- open a browser with Playwright
- search YouTube for `funny cat videos`
- collect up to 10 videos
- save metadata to `youtube_data/videos.csv`
- generate `youtube_data/gallery.html`

If you want the script to download videos, set `DOWNLOAD_VIDEOS = True` inside `Playwright/assignment.py`.

### Selenium tests

```bash
python3 Selenium/assignment.py
```

This runs all Selenium test functions sequentially.

### PyAutoGUI YouTube search

```bash
python3 PyAutoGUI/assignment.py
```

This script uses desktop automation on macOS and opens Chrome to perform a YouTube search.

## View the generated gallery

Open `youtube_data/gallery.html` directly in a browser, or use the VS Code Live Server extension:

1. Install Live Server in VS Code.
2. Open `youtube_data/gallery.html`.
3. Right-click and choose `Open with Live Server`.

## Notes

- `Playwright/assignment.py` requires a working Playwright installation.
- `PyAutoGUI/assignment.py` is macOS-specific and uses screen coordinates.
- `yt-dlp` is only used when `DOWNLOAD_VIDEOS` is enabled.
