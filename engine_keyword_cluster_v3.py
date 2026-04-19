import random

# ----------------------------
# KEYWORD CLUSTERS (TOPICAL AUTHORITY BUILDING)
# ----------------------------

CLUSTERS = {
    "cheap flights": [
        "cheap flights USA to Europe",
        "cheap flights UK to Asia",
        "budget international flights",
        "low cost airline tickets 2026"
    ],
    "flight deals": [
        "best flight deals today",
        "last minute flight deals",
        "Skyscanner flight offers",
        "discount airfare alerts"
    ],
    "travel hacks": [
        "how to book cheap flights",
        "best time to buy airline tickets",
        "flight price prediction tips",
        "hidden airline discount tricks"
    ],
    "destination guides": [
        "cheap countries to visit",
        "budget Europe travel guide",
        "Asia travel on a budget",
        "affordable beach vacations"
    ]
}

# ----------------------------
# PICK CLUSTER FOR TOPIC AUTHORITY
# ----------------------------

def get_cluster(topic_count=50):

    keys = list(CLUSTERS.keys())
    output = []

    for _ in range(topic_count):
        category = random.choice(keys)
        keyword = random.choice(CLUSTERS[category])
        output.append((category, keyword))

    return output

# ----------------------------
# BUILD INTERNAL LINK GRAPH MAP
# ----------------------------

def build_link_graph():

    graph = {}

    for category, keywords in CLUSTERS.items():
        for keyword in keywords:
            graph[keyword] = [k for k in keywords if k != keyword]

    return graph

# ----------------------------
# SEO AUTHORITY BOOST REPORT
# ----------------------------

def seo_report():

    print("SEO Cluster System Active")
    print("Total Clusters:", len(CLUSTERS))
    print("Total Keywords:", sum(len(v) for v in CLUSTERS.values()))

# ----------------------------
# RUN
# ----------------------------

if __name__ == "__main__":
    seo_report()
