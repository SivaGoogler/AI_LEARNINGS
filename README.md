# AI_LEARNINGS

A small automation learning repository with the following scripts:

- `test_playwright.py` — YouTube search scraper using Playwright, saves results to `youtube_data/videos.csv`, generates `youtube_data/gallery.html`, and optionally downloads videos via `yt-dlp`.
- `test_case_selenium.py` — Selenium UI tests against `https://the-internet.herokuapp.com` covering login, checkboxes, dropdown, and dynamic loading.
- `youtube_search_pyautogui.py` — Simple macOS desktop automation using PyAutoGUI to open Chrome, navigate to YouTube, search, and click a video.

## Repository structure

- `test_playwright.py`
- `test_case_selenium.py`
- `youtube_search_pyautogui.py`
- `youtube_data/`
  - `gallery.html`
  - `videos.csv`
  - `videos/`

## Setup

1. Install Python 3.
2. Install required packages:

```bash
python3 -m pip install playwright selenium pyautogui yt-dlp
```

3. Install Playwright browser dependencies:

```bash
python3 -m playwright install
```

## Run the scripts

### Playwright YouTube bot

```bash
python3 test_playwright.py
```

This will:
- open a browser with Playwright
- search YouTube for `funny cat videos`
- collect up to 10 videos
- save metadata to `youtube_data/videos.csv`
- generate `youtube_data/gallery.html`

If you want the script to download videos, set `DOWNLOAD_VIDEOS = True` inside `test_playwright.py`.

### Selenium tests

```bash
python3 test_case_selenium.py
```

This runs all Selenium test functions sequentially.

### PyAutoGUI YouTube search

```bash
python3 youtube_search_pyautogui.py
```

This script uses desktop automation on macOS and opens Chrome to perform a YouTube search.

## View the generated gallery

Open `youtube_data/gallery.html` directly in a browser, or use the VS Code Live Server extension:

1. Install Live Server in VS Code.
2. Open `youtube_data/gallery.html`.
3. Right-click and choose `Open with Live Server`.

## Notes

- `test_playwright.py` requires a working Playwright installation.
- `youtube_search_pyautogui.py` is macOS-specific and uses screen coordinates.
- `yt-dlp` is only used when `DOWNLOAD_VIDEOS` is enabled.
