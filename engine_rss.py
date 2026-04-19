import os
from datetime import datetime

ARTICLE_DIR = "articles"

# IMPORTANT: replace this with your real domain when ready
BASE_URL = "https://yourdomain.com/articles"

def run():
    items = ""

    # loop through generated HTML articles
    for file in os.listdir(ARTICLE_DIR):
        if file.endswith(".html"):
            url = f"{BASE_URL}/{file}"
            title = file.replace(".html", "").replace("_", " ")

            items += f"""
<item>
    <title>{title}</title>
    <link>{url}</link>
    <description>Skyscanner travel deals and flight guide</description>
    <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
</item>
"""

    rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>Skyscanner Travel Deals Feed</title>
    <link>{BASE_URL}</link>
    <description>Daily flight deals and travel guides</description>

    {items}

</channel>
</rss>
"""

    with open("feed.xml", "w", encoding="utf-8") as f:
        f.write(rss)

    print("RSS feed generated: feed.xml")

if __name__ == "__main__":
    run()
