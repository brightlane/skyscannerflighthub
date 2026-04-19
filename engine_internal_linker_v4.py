import os
import random
from engine_keyword_cluster_v3 import CLUSTERS

ARTICLE_DIR = "articles"

# ----------------------------
# BUILD LINK MAP
# ----------------------------

def build_link_map():

    link_map = {}

    for category, keywords in CLUSTERS.items():
        for keyword in keywords:
            link_map[keyword] = [
                k for k in keywords if k != keyword
            ]

    return link_map

# ----------------------------
# GENERATE INTERNAL LINKS HTML
# ----------------------------

def generate_links(keyword, link_map):

    if keyword not in link_map:
        return ""

    links = random.sample(link_map[keyword], min(3, len(link_map[keyword])))

    html = "<h3>Related Travel Topics</h3><ul>"

    for link in links:
        slug = link.replace(" ", "-")
        html += f'<li><a href="/articles/{slug}.html">{link}</a></li>'

    html += "</ul>"

    return html

# ----------------------------
# INJECT INTO HTML FILES
# ----------------------------

def inject_links():

    link_map = build_link_map()

    files = [f for f in os.listdir(ARTICLE_DIR) if f.endswith(".html")]

    for file in files:

        path = os.path.join(ARTICLE_DIR, file)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # pick keyword from filename or fallback
        base_name = file.replace(".html", "").replace("us_", "").replace("uk_", "").replace("eu_", "")
        base_name = base_name.replace("-", " ")

        links_html = generate_links(base_name, link_map)

        # inject before </body>
        if "</body>" in content:
            content = content.replace("</body>", links_html + "\n</body>")

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        print("Linked:", file)

# ----------------------------
# RUN
# ----------------------------

if __name__ == "__main__":
    inject_links()
