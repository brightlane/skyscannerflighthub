import os
import random
import datetime

# Directory where articles will be stored
ARTICLE_DIR = 'articles'
os.makedirs(ARTICLE_DIR, exist_ok=True)

# Your affiliate link
affiliate_link = "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885"

# Dynamic article content generation
def generate_article(number):
    themes = [
        "Find the best flight deals for your next adventure with Skyscanner!",
        "Skyscanner is the easiest way to book your flights and find amazing travel deals.",
        "Get the best discounts and offers on flights with Skyscanner’s unique platform.",
        "Skyscanner is a great tool for travelers looking to compare flights and find the cheapest tickets."
    ]

    theme = random.choice(themes)

    body_content = f"""
    {theme} Skyscanner compares prices from over 1,200 airlines and online travel agencies, ensuring that you find the best deals for your journey.
    Whether you're booking a one-way flight, a return ticket, or a multi-city trip, Skyscanner provides flexibility and convenience.
    
    In addition to finding the lowest fares, Skyscanner also allows you to filter search results based on specific airlines, travel dates, and flight duration.
    You can also sign up for price alerts, ensuring you never miss out on the best price.

    Additionally, Skyscanner offers information on baggage allowances, seat selection fees, and customer reviews, giving you more insight into your travel options.
    
    Take advantage of Skyscanner's best features to book your next trip today! {affiliate_link}
    """

    return body_content

# Function to generate the HTML file and save it
def generate_html_article(article_number):
    today = datetime.date.today()
    article_title = f"Skyscanner_Article_{today}_{article_number}.html"
    
    article_content = generate_article(article_number)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skyscanner Daily Article - {today}</title>
    </head>
    <body>
        <header>
            <h1>Skyscanner Daily Travel Tips</h1>
        </header>
        
        <main>
            <h2>Why Skyscanner is Your Go-To Travel Partner</h2>
            <p>{article_content}</p>
        </main>
        
        <footer>
            <p>Thank you for reading! Visit <a href="{affiliate_link}" target="_blank">Skyscanner</a> for amazing travel deals.</p>
        </footer>
    </body>
    </html>
    """

    article_path = os.path.join(ARTICLE_DIR, article_title)
    with open(article_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Article generated: {article_title}")

# Generate 288 articles
def generate_bulk_articles():
    for i in range(1, 289):
        generate_html_article(i)

if __name__ == "__main__":
    generate_bulk_articles()
