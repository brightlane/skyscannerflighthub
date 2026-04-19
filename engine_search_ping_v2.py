import requests
import os

# ----------------------------
# CONFIG
# ----------------------------

BASE_URL = "https://yourdomain.com/articles"
ARTICLE_DIR = "articles"

# ----------------------------
# COLLECT NEW URLS
# ----------------------------

def get_urls():

    urls = []

    for file in os.listdir(ARTICLE_DIR):
        if file.endswith(".html"):
            urls.append(f"{BASE_URL}/{file}")

    return urls

# ----------------------------
# PING GOOGLE
# ----------------------------

def ping_google(sitemap_url):

    try:
        url = f"https://www.google.com/ping?sitemap={sitemap_url}"
        requests.get(url, timeout=10)
        print("Pinged Google:", sitemap_url)
    except Exception as e:
        print("Google ping failed:", e)

# ----------------------------
# PING BING
# ----------------------------

def ping_bing(sitemap_url):

    try:
        url = f"https://www.bing.com/ping?sitemap={sitemap_url}"
        requests.get(url, timeout=10)
        print("Pinged Bing:", sitemap_url)
    except Exception as e:
        print("Bing ping failed:", e)

# ----------------------------
# OPTIONAL: INDEXNOW (BING FAST INDEX)
# ----------------------------

def indexnow(urls):

    endpoint = "https://api.indexnow.org/indexnow"

    payload = {
        "host": "yourdomain.com",
        "key": "YOUR_INDEXNOW_KEY",
        "urlList": urls
    }

    try:
        requests.post(endpoint, json=payload, timeout=10)
        print("IndexNow submitted")
    except Exception as e:
        print("IndexNow failed:", e)

# ----------------------------
# MAIN RUNNER
# ----------------------------

def run():

    urls = get_urls()

    sitemap_url = f"{BASE_URL}/sitemap.xml"

    # Ping search engines
    ping_google(sitemap_url)
    ping_bing(sitemap_url)

    # Optional fast indexing system
    indexnow(urls)

# ----------------------------
# EXECUTE
# ----------------------------

if __name__ == "__main__":
    run()
