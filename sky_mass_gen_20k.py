import os
import random

# --- SETTINGS ---
TOTAL_PAGES = 20000 
OUTPUT_DIR = "usa_skyscanner_pages"
DOMAIN = "https://yourtravelsite.com"  # Change to your real domain

# --- DATA MATRICES ---
hubs = [
    ("New York", "JFK", "NY"), ("Los Angeles", "LAX", "CA"), ("Chicago", "ORD", "IL"),
    ("Houston", "IAH", "TX"), ("Phoenix", "PHX", "AZ"), ("Philadelphia", "PHL", "PA"),
    ("San Antonio", "SAT", "TX"), ("San Diego", "SAN", "CA"), ("Dallas", "DFW", "TX"),
    ("San Jose", "SJC", "CA"), ("Austin", "AUS", "TX"), ("Jacksonville", "JAX", "FL"),
    ("San Francisco", "SFO", "CA"), ("Columbus", "CMH", "OH"), ("Charlotte", "CLT", "NC"),
    ("Indianapolis", "IND", "IN"), ("Seattle", "SEA", "WA"), ("Denver", "DEN", "CO"),
    ("Washington", "IAD", "DC"), ("Boston", "BOS", "MA"), ("Nashville", "BNA", "TN")
]

destinations = ["London", "Tokyo", "Paris", "Rome", "Cancun", "Dubai", "Bangkok", "Berlin"]
airlines = ["Delta", "United", "American", "Southwest", "JetBlue", "Spirit", "Frontier"]

# --- LAYOUT 1: MODERN DASHBOARD ---
def get_layout_one(city, code, state, i):
    price = random.randint(299, 899)
    airline = random.choice(airlines)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Skyscanner {city} ({code}) - 2026 Flight Deals</title>
    <style>
        body{{font-family:'Segoe UI',sans-serif; margin:0; background:#f4f7f6; color:#333;}}
        .nav{{background:#0071eb; color:white; padding:15px 50px; font-weight:bold;}}
        .hero{{background:white; max-width:1000px; margin:30px auto; padding:40px; border-radius:15px; box-shadow:0 4px 20px rgba(0,0,0,0.08);}}
        .price-box{{display:inline-block; background:#00d3ad; color:#071126; padding:10px 20px; border-radius:5px; font-weight:bold;}}
        .grid{{display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:20px; margin-top:30px;}}
        .card{{background:#fff; border:1px solid #eee; padding:20px; border-radius:10px;}}
        .btn{{display:block; text-align:center; background:#0071eb; color:white; padding:15px; text-decoration:none; border-radius:8px; margin-top:30px;}}
    </style>
</head>
<body>
    <div class="nav">TravelSavvy USA 2026</div>
    <div class="hero">
        <h1>Skyscanner {city} Departures</h1>
        <p>Current analysis for <strong>{state}</strong> flyers. Top value found on <strong>{airline}</strong>.</p>
        <div class="price-box">Best Fare: ${price} round-trip</div>
        <div class="grid">
            <div class="card"><strong>{random.choice(destinations)}</strong><br>From ${random.randint(300,500)}</div>
            <div class="card"><strong>{random.choice(destinations)}</strong><br>From ${random.randint(501,900)}</div>
            <div class="card"><strong>{random.choice(destinations)}</strong><br>From ${random.randint(200,400)}</div>
        </div>
        <a href="https://www.skyscanner.com/transport/flights-from/{code.lower()}" class="btn">View All {code} Deals</a>
        <p style="font-size:10px; color:#ccc; margin-top:20px;">Node ID: {i}-ALPHA</p>
    </div>
</body></html>"""

# --- LAYOUT 2: MINIMALIST ARTICLE ---
def get_layout_two(city, code, state, i):
    days = random.randint(21, 55)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flying from {city} {code} in 2026: Skyscanner Tips</title>
    <style>
        body{{line-height:1.8; color:#444; max-width:800px; margin:0 auto; padding:60px 20px; background:#fff;}}
        h1{{color:#222; border-bottom:2px solid #0071eb; padding-bottom:10px;}}
        .tip-box{{background:#eef6ff; padding:25px; border-radius:10px; margin:30px 0; border-left:5px solid #0071eb;}}
        .footer{{font-size:12px; color:#999; margin-top:50px; border-top:1px solid #eee; padding-top:20px;}}
    </style>
</head>
<body>
    <h1>How to Hack Skyscanner {city} Flights</h1>
    <p>Our 2026 travel audit for <strong>{city}, {state}</strong> indicates a massive shift in airline pricing algorithms.</p>
    <div class="tip-box">
        <strong>Expert Insight:</strong> For {code} departures, Skyscanner users are seeing 15% lower rates when booking exactly {days} days before departure.
    </div>
    <p>Focusing on {random.choice(airlines)} and regional partners allows you to maximize the "Everywhere" search feature from {city}.</p>
    <a href="https://www.skyscanner.com/flights-from/{code.lower()}">Check {city} Prices Now</a>
    <div class="footer">Reference Batch: {i}-BETA | Data Refresh 2026</div>
</body></html>"""

# --- EXECUTION ENGINE ---
def run_generator():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    generated_files = []
    
    print(f"🚀 Starting generation of {TOTAL_PAGES} unique pages...")
    
    for i in range(1, TOTAL_PAGES + 1):
        city, code, state = random.choice(hubs)
        # Create a unique filename for every single page
        file_name = f"skyscanner-2026-{code.lower()}-deals-{i}.html"
        
        # Switch layouts every other page to ensure structural uniqueness
        if i % 2 == 0:
            content = get_layout_one(city, code, state, i)
        else:
            content = get_layout_two(city, code, state, i)
            
        with open(os.path.join(OUTPUT_DIR, file_name), "w", encoding="utf-8") as f:
            f.write(content)
        
        generated_files.append(file_name)
        
        if i % 2000 == 0:
            print(f"✅ Progress: {i} pages created...")

    # --- SITEMAP GENERATION ---
    print("🗺️ Creating Sitemap...")
    with open("sitemap_batch_20k.xml", "w", encoding="utf-8") as s:
        s.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        s.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for f_name in generated_files:
            s.write(f'  <url>\n    <loc>{DOMAIN}/{f_name}</loc>\n    <priority>0.7</priority>\n  </url>\n')
        s.write('</urlset>')

    print(f"✨ SUCCESS: {TOTAL_PAGES} pages in '{OUTPUT_DIR}' and sitemap generated.")

if __name__ == "__main__":
    run_generator()
