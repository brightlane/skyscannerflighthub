import os
import datetime
import random
import schedule
import time
from flask import Flask, send_from_directory

# Set up Flask
app = Flask(__name__)

# Directory to save articles
ARTICLE_DIR = 'generated_articles'
os.makedirs(ARTICLE_DIR, exist_ok=True)

# Your affiliate link
affiliate_link = "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885"

# Generate a 400-word article about Skyscanner
def generate_article():
    # List of daily article introductions about Skyscanner
    introductions = [
        "Skyscanner is a popular travel search engine that helps you find the best flight deals.",
        "Looking for a cheap flight? Skyscanner is one of the most trusted platforms to compare airfares.",
        "Skyscanner allows you to search for flights, hotels, and car rentals in one place, helping you save time and money.",
        "Skyscanner is a great tool for finding flights, hotels, and even car rentals, offering a seamless travel experience."
    ]
    
    # Randomly select an introduction
    intro = random.choice(introductions)

    # Create a 400-word article (expandable content)
    body_content = f"""
    {intro} It compares prices from over 1,200 airlines and online travel agencies, ensuring that you find the best deals.
    Skyscanner's platform is user-friendly, allowing you to filter flights based on departure times, airlines, and other preferences. 
    Whether you're booking in advance or looking for last-minute deals, Skyscanner is a fantastic resource.
    
    One of the best features of Skyscanner is its flexibility. You can search for flights on specific dates or use the flexible dates feature to find the lowest prices across a range of dates. Additionally, it offers a multi-city option for travelers looking to book more complex itineraries.

    Skyscanner also provides useful information such as baggage policies, seat selection fees, and flight reviews. With this information, travelers can make more informed decisions about their flights.

    Another great aspect is the ability to set price alerts. If the price of a flight drops, Skyscanner will send you an email notification, helping you take advantage of price fluctuations.

    In conclusion, Skyscanner is an excellent resource for travelers seeking the best flight deals. Whether you're planning a short trip or a long-haul adventure, Skyscanner has you covered. {affiliate_link}
    """
    
    return body_content

# Function to generate the HTML file and save it to disk
def generate_html_article():
    # Get the current date to name the article
    today = datetime.date.today()
    article_title = f"Skyscanner_Article_{today}.html"
    
    # Generate the article content
    article_content = generate_article()

    # HTML structure for the article
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
    
    # Save the article in the generated_articles folder
    article_path = os.path.join(ARTICLE_DIR, article_title)
    with open(article_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Article generated: {article_title}")

# Set up a Flask route to serve generated articles
@app.route('/articles/<filename>')
def serve_article(filename):
    return send_from_directory(ARTICLE_DIR, filename)

# Schedule the task to run daily at a specific time (e.g., 7:00 AM)
def schedule_daily_task():
    schedule.every().day.at("07:00").do(generate_html_article)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

# Run Flask app and scheduling task in parallel
if __name__ == "__main__":
    # Start the scheduling task in a separate thread
    import threading
    task_thread = threading.Thread(target=schedule_daily_task)
    task_thread.start()
    
    # Start the Flask web server
    app.run(debug=True, use_reloader=False)  # use_reloader=False to prevent running the task twice
