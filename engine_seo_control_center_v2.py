import os
import requests

# ----------------------------
# CONFIG
# ----------------------------

BASE_URL = "https://yourdomain.com/articles"
SITEMAP = f"{BASE_URL}/sitemap.xml"

ARTICLE_DIR = "articles"

# ----------------------------
# COLLECT ALL URLS
# ----------------------------

def collect_urls():

    urls = []

    for file in os.listdir(ARTICLE_DIR):
        if file.endswith(".html"):
            urls.append(f"{BASE_URL}/{file}")

    return urls

# ----------------------------
# GOOGLE PING
# ----------------------------

def ping_google():

    try:
        url = f"https://www.google.com/ping?sitemap={SITEMAP}"
        requests.get(url, timeout=10)
        print("Google sitemap ping sent")
    except Exception as e:
        print("Google ping error:", e)

# ----------------------------
# BING PING
# ----------------------------

def ping_bing():

    try:
        url = f"https://www.bing.com/ping?sitemap={SITEMAP}"
        requests.get(url, timeout=10)
        print("Bing sitemap ping sent")
    except Exception as e:
        print("Bing ping error:", e)

# ----------------------------
# INDEXNOW (FAST INDEXING)
# ----------------------------

def indexnow():

    urls = collect_urls()

    payload = {
        "host": "yourdomain.com",
        "key": "YOUR_INDEXNOW_KEY",
        "urlList": urls
    }

    try:
        requests.post("https://api.indexnow.org/indexnow", json=payload, timeout=10)
        print("IndexNow submitted:", len(urls), "urls")
    except Exception as e:
        print("IndexNow error:", e)

# ----------------------------
# SEO HEALTH CHECK (OPTIONAL)
# ----------------------------

def health_check():

    total = len(collect_urls())
    print(f"Total indexed pages (generated): {total}")

# ----------------------------
# MAIN RUNNER
# ----------------------------

def run():

    print("Starting SEO Control Center...")

    health_check()
    ping_google()
    ping_bing()
    indexnow()

    print("SEO Control Center finished")

# ----------------------------
# EXECUTE
# ----------------------------

if __name__ == "__main__":
    run()
