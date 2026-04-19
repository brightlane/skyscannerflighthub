import os

# ----------------------------
# CONFIG
# ----------------------------

BASE_URL = "https://yourdomain.com/articles"
ARTICLE_DIR = "articles"

# ----------------------------
# COLLECT FILES BY REGION
# ----------------------------

def collect_files():
    regions = {
        "us": [],
        "uk": [],
        "eu": []
    }

    for file in os.listdir(ARTICLE_DIR):
        if file.endswith(".html"):

            if file.startswith("us_"):
                regions["us"].append(file)
            elif file.startswith("uk_"):
                regions["uk"].append(file)
            elif file.startswith("eu_"):
                regions["eu"].append(file)

    return regions

# ----------------------------
# BUILD SITEMAP XML
# ----------------------------

def build_sitemap(files):

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for file in files:
        xml += f"""
    <url>
        <loc>{BASE_URL}/{file}</loc>
    </url>
"""

    xml += "</urlset>"
    return xml

# ----------------------------
# MAIN RUNNER
# ----------------------------

def run():

    regions = collect_files()

    # Generate main combined sitemap (recommended for SEO)
    all_files = regions["us"] + regions["uk"] + regions["eu"]

    sitemap = build_sitemap(all_files)

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

    print("Generated: sitemap.xml")

    # OPTIONAL: region-specific sitemaps (advanced SEO)
    for region, files in regions.items():

        if files:

            region_sitemap = build_sitemap(files)

            with open(f"sitemap-{region}.xml", "w", encoding="utf-8") as f:
                f.write(region_sitemap)

            print(f"Generated: sitemap-{region}.xml")

# ----------------------------
# EXECUTE
# ----------------------------

if __name__ == "__main__":
    run()
