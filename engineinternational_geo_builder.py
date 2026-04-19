import os
from engines_geo_feeder import generate_geo_topics
from engine_geo_variation import region_text, title_variant

# Your affiliate link
AFFILIATE = "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885"

# Base URL (CHANGE THIS to your domain or GitHub Pages URL)
BASE_URL = "https://yourdomain.com/articles"

os.makedirs("articles", exist_ok=True)

# ----------------------------
# HREFLANG BLOCK (SEO IMPORTANT)
# ----------------------------
def hreflang_block(file_name):
    return f"""
<link rel="alternate" hreflang="en-us" href="{BASE_URL}/us/{file_name}">
<link rel="alternate" hreflang="en-gb" href="{BASE_URL}/uk/{file_name}">
<link rel="alternate" hreflang="en-eu" href="{BASE_URL}/eu/{file_name}">
<link rel="alternate" hreflang="x-default" href="{BASE_URL}/{file_name}">
"""

# ----------------------------
# INTERNAL LINKS (SEO BOOST)
# ----------------------------
def internal_links(slug):
    return f"""
<h3>Explore more travel guides</h3>
<ul>
  <li><a href="{BASE_URL}/us/{slug}">USA version</a></li>
  <li><a href="{BASE_URL}/uk/{slug}">UK version</a></li>
  <li><a href="{BASE_URL}/eu/{slug}">Europe version</a></li>
</ul>
"""

# ----------------------------
# BUILD ARTICLE
# ----------------------------
def build_article(region, title, file_name):

    seo_text = region_text(region)
    hreflang = hreflang_block(file_name)
    links = internal_links(file_name)

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>

{hreflang}

<meta name="description" content="{title} - Skyscanner travel deals and flight savings guide">

</head>

<body>

<h1>{title}</h1>

<p>
{seo_text}. This guide helps travelers find cheaper flights using comparison tools like Skyscanner.
</p>

<h2>Best Travel Strategy</h2>
<p>
Always compare flexible dates, nearby airports, and alternative routes to reduce flight costs.
</p>

<h2>Find Real Flight Deals</h2>
<p>
<a href="{AFFILIATE}" target="_blank">Search Skyscanner Live Prices</a>
</p>

{links}

<h2>Final Tip</h2>
<p>
Prices change daily — checking multiple times can save significant money.
</p>

</body>
</html>
"""

# ----------------------------
# MAIN RUNNER
# ----------------------------
def run():
    topics = generate_geo_topics(30)

    for i, (region, base_title) in enumerate(topics):

        # region-specific title
        title = title_variant(base_title, region)

        file_name = f"{region}_{i}.html"

        file_path = f"articles/{file_name}"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(build_article(region, title, file_name))

        print("Created:", file_name)

if __name__ == "__main__":
    run()
