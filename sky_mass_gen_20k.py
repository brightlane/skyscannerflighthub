import os
import random

# ==========================================
# 1. SETTINGS & CONFIGURATION
# ==========================================
TOTAL_PAGES = 20000 
OUTPUT_DIR = "usa_skyscanner_pages"
DOMAIN = "https://yourtravelsite.com"  # Replace with your actual domain

# Replace with your actual Impact/Travelpayouts/Skyscanner base URL
# Example: https://skyscanner.pxf.io/c/123456/7890/
BASE_AFF_URL = "PASTE_YOUR_AFFILIATE_URL_HERE"

# ==========================================
# 2. DATA MATRICES (Expanded for 20k diversity)
# ==========================================
hubs = [
    ("New York", "JFK", "NY"), ("Los Angeles", "LAX", "CA"), ("Chicago", "ORD", "IL"),
    ("Houston", "IAH", "TX"), ("Phoenix", "PHX", "AZ"), ("Philadelphia", "PHL", "PA"),
    ("San Antonio", "SAT", "TX"), ("San Diego", "SAN", "CA"), ("Dallas", "DFW", "TX"),
    ("San Jose", "SJC", "CA"), ("Austin", "AUS", "TX"), ("Jacksonville", "JAX", "FL"),
    ("San Francisco", "SFO", "CA"), ("Columbus", "CMH", "OH"), ("Charlotte", "CLT", "NC"),
    ("Indianapolis", "IND", "IN"), ("Seattle", "SEA", "WA"), ("Denver", "DEN", "CO"),
    ("Washington", "IAD", "DC"), ("Boston", "BOS", "MA"), ("Nashville", "BNA", "TN"),
    ("Miami", "MIA", "FL"), ("Atlanta", "ATL", "GA"), ("Detroit", "DTW", "MI"),
    ("Orlando", "MCO", "FL"), ("Las Vegas", "LAS", "NV"), ("Portland", "PDX", "OR")
]

destinations = ["London", "Tokyo", "Paris", "Rome", "Cancun", "Dubai", "Bangkok", "Berlin", "Barcelona", "Seoul"]
airlines = ["Delta", "United", "American", "Southwest", "JetBlue", "Spirit", "Frontier", "Alaska Airlines"]
hooks = [
    "Exclusive 2026 Price Audit", "Real-time Inventory Reset", 
    "Hidden Fare Discovery", "Last-Minute Hub Analysis"
]

# ==========================================
# 3. PAGE BUILDER ENGINE
# ==========================================

def get_aff_link(code):
    """Constructs a deep-linked affiliate URL for a specific origin code."""
    # This structure works for most modern affiliate redirects (Net/Impact)
    return f"{BASE_AFF_URL}?u=https://www.skyscanner.com/transport/flights-from/{code.lower()}"

def get_layout_one(city, code, state, i):
    price = random.randint(312, 945)
    airline = random.choice(airlines)
    aff_link = get_aff_link(code)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Skyscanner {city} ({code}) - {random.choice(hooks)} 2026</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{{font-family:'Helvetica Neue',sans-serif; margin:0; background:#f0f4f8; color:#1a202c;}}
        .navbar{{background:#0071eb; color:white; padding:20px; text-align:center; font-weight:bold; letter-spacing:1px;}}
        .main-card{{background:white; max-width:900px; margin:40px auto; padding:50px; border-radius:20px; box-shadow:0 15px 35px rgba(0,0,0,0.1);}}
        .price-badge{{display:inline-block; background:#00d3ad; color:#071126; padding:12px 24px; border-radius:50px; font-size:22px; font-weight:900; margin-bottom:20px;}}
        .grid{{display:grid; grid-template-columns:repeat(auto-fit, minmax(250px, 1fr)); gap:25px; margin-top:40px;}}
        .item{{background:#f8fafc; border:1px solid #e2e8f0; padding:25px; border-radius:15px; transition:0.3s;}}
        .item:hover{{transform:translateY(-5px); border-color:#0071eb;}}
        .cta-btn{{display:block; text-align:center; background:#0071eb; color:white; padding:20px; text-decoration:none; border-radius:12px; font-size:18px; font-weight:bold; margin-top:40px; transition:0.3s;}}
        .cta-btn:hover{{background:#0056b3;}}
        .footer{{text-align:center; font-size:11px; color:#a0aec0; margin-top:50px;}}
    </style>
</head>
<body>
    <div class="navbar">STADIUMSTAY GLOBAL TRAVEL | 2026</div>
    <div class="main-card">
        <h1>Skyscanner {city} Hub Report</h1>
        <p>Market Analysis: {state} travelers are currently seeing a price floor reset. <strong>{airline}</strong> has increased frequency from <strong>{code}</strong>.</p>
        <div class="price-badge">Avg. Round Trip: ${price}</div>
        <div class="grid">
            <div class="item"><strong>To {random.choice(destinations)}</strong><br>Check Live Rates</div>
            <div class="item"><strong>To {random.choice(destinations)}</strong><br>Trending: Low Fares</div>
            <div class="item"><strong>To {random.choice(destinations)}</strong><br>New 2026 Routes</div>
        </div>
        <a href="{aff_link}" class="cta-btn">SEARCH ALL {city.upper()} DEALS ON SKYSCANNER</a>
        <div class="footer">Vulture Titan Engine v10.4 | ID: {i}-RUN-A</div>
    </div>
</body></html>"""

def get_layout_two(city, code, state, i):
    days = random.randint(18, 42)
    aff_link = get_aff_link(code)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flying from {city} {code} - Skyscanner Booking Guide 2026</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{{line-height:1.7; color:#2d3748; max-width:850px; margin:0 auto; padding:60px 20px; background:#fff;}}
        h1{{font-size:36px; color:#1a202c; border-bottom:5px solid #ffd700; display:inline-block; margin-bottom:30px;}}
        .insight{{background:#fffaf0; padding:30px; border-radius:15px; border-left:8px solid #ffd700; margin:40px 0; font-size:18px;}}
        .list{{margin:30px 0; padding-left:20px;}}
        .list li{{margin-bottom:15px;}}
        .aff-cta{{display:inline-block; background:#1a202c; color:white; padding:18px 35px; text-decoration:none; border-radius:8px; font-weight:bold; margin-top:20px;}}
        .aff-cta:hover{{background:#4a5568;}}
        .meta{{font-size:12px; color:#cbd5e0; margin-top:80px; border-top:1px solid #edf2f7; padding-top:20px;}}
    </style>
</head>
<body>
    <h1>Optimization Guide: {city} ({code})</h1>
    <p>According to Skyscanner internal trends for 2026, flyers originating in <strong>{state}</strong> are eligible for "Everywhere" search incentives.</p>
    <div class="insight">
        <strong>2026 Strategy:</strong> For the best {city} ({code}) deals, set your search window to exactly {days} days out. This bypasses the standard mid-month price adjustments.
    </div>
    <ul class="list">
        <li>Monitor <strong>{random.choice(airlines)}</strong> for seasonal {code} resets.</li>
        <li>Use the Skyscanner monthly view to pinpoint the ${random.randint(150, 350)} floor price.</li>
        <li>Consider {random.choice(destinations)} as a primary connection hub.</li>
    </ul>
    <a href="{aff_link}" class="aff-cta">Check {city} Prices Now</a>
    <div class="meta">Batch Authorization: {i}-BETA-VULTURE | May 2026 Data Stream</div>
</body></html>"""

# ==========================================
# 4. EXECUTION FLOW
# ==========================================

def run_vulture_engine():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    generated_files = []
    print(f"🔥 VULTURE TITAN STARTING: Generating {TOTAL_PAGES} unique pages...")
    
    for i in range(1, TOTAL_PAGES + 1):
        city, code, state = random.choice(hubs)
        # Unique filename ensures no overwrites
        file_name = f"skyscanner-deals-2026-{code.lower()}-{i}.html"
        
        # Randomly toggle between two structural layouts
        if random.random() > 0.5:
            content = get_layout_one(city, code, state, i)
        else:
            content = get_layout_two(city, code, state, i)
            
        with open(os.path.join(OUTPUT_DIR, file_name), "w", encoding="utf-8") as f:
            f.write(content)
        
        generated_files.append(file_name)
        
        if i % 5000 == 0:
            print(f"✅ Checkpoint: {i} pages indexed...")

    # --- SITEMAP GENERATION ---
    print("🗺️ Generating Sitemaps...")
    with open("sitemap_vulture_20k.xml", "w", encoding="utf-8") as s:
        s.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        s.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for f_name in generated_files:
            s.write(f'  <url>\n    <loc>{DOMAIN}/{f_name}</loc>\n    <changefreq>weekly</changefreq>\n  </url>\n')
        s.write('</urlset>')

    print(f"✨ MISSION COMPLETE. Check folder '{OUTPUT_DIR}' for 20,000 unique pages.")

if __name__ == "__main__":
    run_vulture_engine()
