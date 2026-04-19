import random

# ----------------------------
# REGION-SPECIFIC SEO STYLES
# (This prevents duplicate content issues)
# ----------------------------

US_VARIANTS = [
    "cheap domestic flight deals across the United States",
    "budget airline offers and US travel savings",
    "low-cost flights within America and international routes",
    "Skyscanner deals for USA travelers looking to save money"
]

UK_VARIANTS = [
    "cheap flights from London and UK airports",
    "budget travel deals for UK holidaymakers",
    "low-cost airline tickets from the United Kingdom",
    "Skyscanner UK flight comparison tips and savings"
]

EU_VARIANTS = [
    "cheap flights across Europe and budget travel routes",
    "affordable inter-European airline deals",
    "low-cost travel within European countries",
    "Skyscanner Europe travel hacks for cheaper flights"
]

# ----------------------------
# SELECT REGION TEXT
# ----------------------------

def region_text(region):
    """
    Returns unique SEO-safe text per region.
    This is the key anti-duplicate system.
    """

    if region == "us":
        return random.choice(US_VARIANTS)

    elif region == "uk":
        return random.choice(UK_VARIANTS)

    else:
        return random.choice(EU_VARIANTS)


# ----------------------------
# OPTIONAL: SEO TITLE VARIATION
# ----------------------------

def title_variant(base_title, region):
    prefix = {
        "us": "USA Guide:",
        "uk": "UK Guide:",
        "eu": "Europe Guide:"
    }

    return f"{prefix.get(region, 'Guide:')} {base_title}"
