import random

REGIONS = {
    "us": {
        "prefix": "USA",
        "keywords": ["cheap flights USA", "budget flights America", "US flight deals"]
    },
    "uk": {
        "prefix": "UK",
        "keywords": ["cheap flights UK", "London flight deals", "UK travel deals"]
    },
    "eu": {
        "prefix": "Europe",
        "keywords": ["cheap flights Europe", "EU travel deals", "Europe budget flights"]
    }
}

DESTINATIONS = [
    "to Europe",
    "to Asia",
    "to Middle East",
    "to Africa",
    "to Australia"
]

MODIFIERS = [
    "2026 guide",
    "best deals",
    "cheap tickets",
    "Skyscanner tips",
    "flight hacks"
]

def generate_geo_topics(n=30):
    output = []

    regions = list(REGIONS.keys())

    for _ in range(n):
        region = random.choice(regions)
        dest = random.choice(DESTINATIONS)
        mod = random.choice(MODIFIERS)

        title = f"{REGIONS[region]['prefix']} {random.choice(REGIONS[region]['keywords'])} {dest} {mod}"

        output.append((region, title))

    return output
