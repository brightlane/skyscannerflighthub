import os

BASE = "https://yourdomain.com/articles"

def run():
    sitemaps = {
        "us": [],
        "uk": [],
        "eu": []
    }

    for f in os.listdir("articles"):
        if f.endswith(".html"):
            if f.startswith("us_"):
                sitemaps["us"].append(f)
            elif f.startswith("uk_"):
                sitemaps["uk"].append(f)
            elif f.startswith("eu_"):
                sitemaps["eu"].append(f)

    for region, files in sitemaps.items():

        xml = '<?xml version="1.0"?>\n<urlset>\n'

        for f in files:
            xml += f"<url><loc>{BASE}/{f}</loc></url>\n"

        xml += "</urlset>"

        with open(f"sitemap-{region}.xml", "w") as out:
            out.write(xml)

        print("Generated sitemap:", region)

if __name__ == "__main__":
    run()
