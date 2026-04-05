import os
import time
import csv
import re
from playwright.sync_api import sync_playwright

# =========================
# CONFIG
# =========================
SEARCH_QUERY = "funny cat videos"
MAX_VIDEOS = 10
SCROLL_TIMES = 5
DOWNLOAD_VIDEOS = False   # ⚠️ Set True if you want downloads

OUTPUT_DIR = "youtube_data"
VIDEO_DIR = os.path.join(OUTPUT_DIR, "videos")

# =========================
# SETUP FOLDERS
# =========================
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

# =========================
# HELPERS
# =========================
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_video(url, filename):
    try:
        print(f"⬇️ Downloading: {filename}")
        os.system(f'yt-dlp -o "{filename}" {url}')
    except Exception as e:
        print("Download error:", e)

# =========================
# MAIN BOT
# =========================
def run_bot():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("🌐 Opening YouTube...")
        page.goto(f"https://www.youtube.com/results?search_query={SEARCH_QUERY}")

        page.wait_for_timeout(5000)

        # Scroll to load videos
        print("🔄 Scrolling...")
        for _ in range(SCROLL_TIMES):
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(2000)

        print("🔍 Extracting videos...")
        videos = page.query_selector_all("ytd-video-renderer")

        print(f"📊 Found {len(videos)} videos\n")

        for i, video in enumerate(videos[:MAX_VIDEOS]):
            try:
                title_el = video.query_selector("#video-title")
                thumb_el = video.query_selector("img")

                if not title_el:
                    continue

                title = title_el.inner_text().strip()
                link = title_el.get_attribute("href")

                if not link:
                    continue

                full_link = f"https://www.youtube.com{link}"

                thumbnail = thumb_el.get_attribute("src") if thumb_el else None

                print(f"🎬 {i+1}. {title}")
                print(f"🔗 {full_link}")
                print(f"🖼️ {thumbnail}")
                print("-" * 60)

                results.append({
                    "title": title,
                    "link": full_link,
                    "thumbnail": thumbnail
                })

                # Optional download
                if DOWNLOAD_VIDEOS:
                    safe_title = sanitize_filename(f"{i+1}_{title}.mp4")
                    filepath = os.path.join(VIDEO_DIR, safe_title)
                    download_video(full_link, filepath)

            except Exception as e:
                print("❌ Error processing video:", e)

        browser.close()

    return results

# =========================
# SAVE CSV
# =========================
def save_to_csv(data):
    csv_path = os.path.join(OUTPUT_DIR, "videos.csv")

    print(f"\n💾 Saving data to {csv_path}...")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link", "thumbnail"])
        writer.writeheader()
        writer.writerows(data)

# =========================
# GENERATE HTML
# =========================
def generate_html(data):
    html_path = os.path.join(OUTPUT_DIR, "gallery.html")

    print(f"🌐 Creating HTML gallery: {html_path}")

    html = """
    <html>
    <head>
        <title>YouTube Bot Gallery</title>
    </head>
    <body>
        <h1>🎥 YouTube Video Gallery</h1>
    """

    for item in data:
        html += f"""
        <div style="margin-bottom:20px;">
            <h3>{item['title']}</h3>
            <a href="{item['link']}" target="_blank">
                <img src="{item['thumbnail']}" width="300">
            </a>
        </div>
        """

    html += "</body></html>"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

# =========================
# RUN EVERYTHING
# =========================
if __name__ == "__main__":
    print("🚀 Starting YouTube Bot...\n")

    data = run_bot()

    if data:
        save_to_csv(data)
        generate_html(data)

    print("\n✅ Done!")