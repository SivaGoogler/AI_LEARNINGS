# AI_LEARNINGS

A learning repository covering web automation, testing, and web frameworks:

- `Playwright/assignment.py` — YouTube search scraper using Playwright, saves results to `youtube_data/videos.csv`, generates `youtube_data/gallery.html`, and optionally downloads videos via `yt-dlp`.
- `Selenium/assignment.py` — Selenium UI tests against `https://the-internet.herokuapp.com` covering login, checkboxes, dropdown, and dynamic loading.
- `PyAutoGUI/assignment.py` — macOS desktop automation using PyAutoGUI to open Chrome, navigate to YouTube, search, and click a video.
- `Flask/assignment.py` — Simple RESTful API with math operations (add, subtract, multiply, divide).

## Repository structure

- `Playwright/`
  - `assignment.py`
  - `assignment_details.txt`
- `Selenium/`
  - `assignment.py`
  - `assignment_details.txt`
- `PyAutoGUI/`
  - `assignment.py`
  - `assignment_details.txt`
- `Flask/`
  - `assignment.py`
  - `assignment_details.txt`
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

### Flask Math API

```bash
python3 Flask/assignment.py
```

This will start a Flask development server on `http://localhost:5000`.

## Testing Flask API with Postman

1. **Download and install Postman** from [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

2. **Start the Flask app** (runs on `http://localhost:5000`)

3. **Test the endpoints in Postman:**

#### Health Check (GET)
- **URL**: `http://localhost:5000/`
- **Method**: GET
- **Result**: Returns available endpoints

#### Add (POST)
- **URL**: `http://localhost:5000/add`
- **Method**: POST
- **Header**: Set `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
  "num1": 10,
  "num2": 5
}
```
- **Result**: `{ "operation": "addition", "num1": 10, "num2": 5, "result": 15 }`

#### Subtract (POST)
- **URL**: `http://localhost:5000/subtract`
- **Method**: POST
- **Header**: Set `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
  "num1": 10,
  "num2": 5
}
```
- **Result**: `{ "operation": "subtraction", "result": 5 }`

#### Multiply (POST)
- **URL**: `http://localhost:5000/multiply`
- **Method**: POST
- **Header**: Set `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
  "num1": 10,
  "num2": 5
}
```
- **Result**: `{ "operation": "multiplication", "result": 50 }`

#### Divide (POST)
- **URL**: `http://localhost:5000/divide`
- **Method**: POST
- **Header**: Set `Content-Type: application/json`
- **Body** (raw JSON):
```json
{
  "num1": 10,
  "num2": 5
}
```
- **Result**: `{ "operation": "division", "result": 2 }`

#### Error Case (Division by Zero)
- **URL**: `http://localhost:5000/divide`
- **Method**: POST
- **Body**:
```json
{
  "num1": 10,
  "num2": 0
}
```
- **Result**: `{ "error": "❌ Cannot divide by zero" }` (HTTP 400)

## View the generated gallery

Open `youtube_data/gallery.html` directly in a browser, or use the VS Code Live Server extension:

1. Install Live Server in VS Code.
2. Open `youtube_data/gallery.html`.
3. Right-click and choose `Open with Live Server`.

## Notes

- `Playwright/assignment.py` requires a working Playwright installation.
- `PyAutoGUI/assignment.py` is macOS-specific and uses screen coordinates.
- `yt-dlp` is only used when `DOWNLOAD_VIDEOS` is enabled.
