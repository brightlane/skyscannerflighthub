import os
import datetime
import random
import schedule
import time

# Your affiliate link to insert into the article
affiliate_link = "https://convert.ctypy.com/aff_c?offer_id=29465&aff_id=21885"

# Template for the article content (this can be more complex if needed)
def generate_article():
    # List of daily article introductions about Skyscanner (you can expand this list)
    introductions = [
        "Skyscanner is a popular travel search engine that helps you find the best flight deals.",
        "Looking for a cheap flight? Skyscanner is one of the most trusted platforms to compare airfares.",
        "Skyscanner allows you to search for flights, hotels, and car rentals in one place, helping you save time and money.",
        "Skyscanner is a great tool for finding flights, hotels, and even car rentals, offering a seamless travel experience."
    ]

    # Randomly select an introduction to make it different every day
    intro = random.choice(introductions)

    # Create a 400-word article (this can be customized with more in-depth content)
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

# Function to generate and save the article as HTML file
def generate_html_article():
    # Get the current date to use in the filename
    today = datetime.date.today()
    article_title = f"Skyscanner_Article_{today}.html"
    
    # Generate the article content
    article_content = generate_article()

    # Define the full HTML structure for the article
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
    
    # Save the HTML file with today's date
    with open(article_title, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Article generated: {article_title}")

# Schedule the job to run once per day at a specific time (e.g., 7:00 AM)
def schedule_daily_task():
    schedule.every().day.at("07:00").do(generate_html_article)

    while True:
        schedule.run_pending()
        time.sleep(60)

# Run the scheduler
if __name__ == "__main__":
    schedule_daily_task()
