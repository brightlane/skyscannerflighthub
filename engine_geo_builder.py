import os
from engines_geo_feeder import generate_geo_topics

AFFILIATE = "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885"

BASE_URL = "https://yourdomain.com/articles"

os.makedirs("articles", exist_ok=True)

def hreflang(region, file):
    return f"""
<link rel="alternate" hreflang="en-{region}" href="{BASE_URL}/{file}">
"""

def build_article(region, title):

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>

<!-- hreflang tags -->
{hreflang("us", "us_"+title+".html")}
{hreflang("gb", "uk_"+title+".html")}
{hreflang("eu", "eu_"+title+".html")}

</head>

<body>

<h1>{title}</h1>

<p>
This guide focuses on {title.lower()} and compares flight prices using Skyscanner and other tools.
</p>

<h2>Best Travel Strategy</h2>
<p>
Prices vary by region, so comparing flexible dates helps you save money.
</p>

<h2>Find Deals</h2>
<p>
<a href="{AFFILIATE}">Search Skyscanner Flights</a>
</p>

</body>
</html>
"""

def run():
    topics = generate_geo_topics(30)

    for i, (region, title) in enumerate(topics):

        file_name = f"{region}_{i}.html"

        with open(f"articles/{file_name}", "w", encoding="utf-8") as f:
            f.write(build_article(region, title))

        print("Created:", file_name)

if __name__ == "__main__":
    run()
