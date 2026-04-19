import random

# Core travel intents
core = [
    "cheap flights",
    "budget flights",
    "flight deals",
    "last minute flights",
    "flight offers",
    "airfare discounts",
    "Skyscanner deals",
    "travel deals",
]

# Destinations
destinations = [
    "USA to Europe",
    "USA to Asia",
    "UK to Spain",
    "UK to USA",
    "Europe to Asia",
    "Canada to Europe",
    "Australia to Thailand",
    "India to Dubai",
    "USA to Africa",
    "Europe to USA"
]

# Modifiers (SEO boosters)
modifiers = [
    "2026 guide",
    "best time to book",
    "cheap tips",
    "money saving tricks",
    "step by step guide",
    "hacks you must know",
    "ultimate guide",
    "hidden secrets",
    "updated deals",
    "for beginners"
]

# Optional Skyscanner branding injection
brands = [
    "Skyscanner",
    "flight comparison",
    "airfare tracker",
    "travel search tools"
]

def generate_topic():
    topic = f"{random.choice(core)} {random.choice(destinations)} {random.choice(modifiers)}"
    return topic

def generate_batch(n=50):
    return [generate_topic() for _ in range(n)]
