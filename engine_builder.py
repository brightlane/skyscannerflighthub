import os
from engines_feeder import generate_topics  # ✅ updated name

# Your affiliate link
AFFILIATE_LINK = "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885"

# Folder where articles go
ARTICLE_DIR = "articles"
os.makedirs(ARTICLE_DIR, exist_ok=True)

# ----------------------------
# Build SEO article template
# ----------------------------
def build_article(title, category):

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta name="description" content="{title} travel guide and Skyscanner flight deals">
</head>

<body>

<h1>{title}</h1>

<p>
Looking for the best deals on {title.lower()}? This guide shows you how to save money using flight comparison tools like Skyscanner.
</p>

<h2>Overview</h2>
<p>
Travel prices change daily. Using smart search strategies helps you find cheaper flights and better routes.
</p>

<h2>Top Tips</h2>
<ul>
    <li>Compare flexible dates</li>
    <li>Book early or last-minute deals</li>
    <li>Use price alerts</li>
</ul>

<h2>Why Use Skyscanner</h2>
<p>
Skyscanner helps compare hundreds of airlines and travel routes in seconds.
</p>

<h2>Find Real Deals</h2>
<p>
<a href="{AFFILIATE_LINK}" target="_blank">Check Skyscanner Flight Prices</a>
</p>

<h2>Final Advice</h2>
<p>
Always compare multiple routes before booking to get the lowest fare.
</p>

</body>
</html>
"""

# ----------------------------
# MAIN RUN FUNCTION
# ----------------------------
def run():
    topics = generate_topics(50)  # number of articles per run

    for i, (category, title) in enumerate(topics):
        file_path = f"{ARTICLE_DIR}/article_{i}.html"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(build_article(title, category))

        print(f"Created: {title}")

# Run script
if __name__ == "__main__":
    run()
