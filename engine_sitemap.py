import os

# IMPORTANT: replace this with your real domain
BASE_URL = "https://yourdomain.com/articles"

ARTICLE_DIR = "articles"

def run():
    urls = []

    # collect all article pages
    for file in os.listdir(ARTICLE_DIR):
        if file.endswith(".html"):
            urls.append(f"{BASE_URL}/{file}")

    # build XML sitemap
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        xml += f"""
    <url>
        <loc>{url}</loc>
    </url>
"""

    xml += "</urlset>"

    # save file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)

    print("Sitemap generated: sitemap.xml")

if __name__ == "__main__":
    run()
