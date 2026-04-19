import random

clusters = {
    "cheap flights": [
        "cheap flights USA to Europe",
        "cheap flights UK to Asia",
        "budget flights from Canada",
        "low cost flights 2026"
    ],
    "travel deals": [
        "best flight deals today",
        "last minute travel deals",
        "flash flight sales",
        "Skyscanner travel offers"
    ],
    "destination guides": [
        "cheap countries to visit",
        "budget Europe travel guide",
        "Asia on a budget",
        "affordable beach holidays"
    ],
    "travel hacks": [
        "how to save money on flights",
        "best time to book flights",
        "flight booking secrets",
        "cheap airfare tricks"
    ]
}

def generate_topics(n=50):
    topics = []

    keys = list(clusters.keys())

    for _ in range(n):
        category = random.choice(keys)
        topic = random.choice(clusters[category])
        topics.append((category, topic))

    return topics
