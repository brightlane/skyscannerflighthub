import os
import datetime
import xml.etree.ElementTree as ET

# Path to articles
ARTICLE_DIR = 'articles'
FEED_FILE = 'feed.xml'

# Define the base URL of your site (make sure this is correct)
BASE_URL = 'https://example.com/articles'

# Function to generate the RSS feed
def generate_rss_feed():
    # Create the root element for the RSS feed
    rss = ET.Element('rss', version="2.0")
    channel = ET.SubElement(rss, 'channel')

    # Add some basic channel info (you can customize these)
    ET.SubElement(channel, 'title').text = 'Skyscanner Travel Articles'
    ET.SubElement(channel, 'link').text = BASE_URL
    ET.SubElement(channel, 'description').text = 'Daily articles on Skyscanner travel deals'

    # Loop through articles in the `articles/` folder
    for filename in os.listdir(ARTICLE_DIR):
        if filename.endswith('.html'):
            article_path = os.path.join(ARTICLE_DIR, filename)
            article_url = BASE_URL + '/' + filename

            # Add an <item> element for each article
            item = ET.SubElement(channel, 'item')
            ET.SubElement(item, 'title').text = filename.replace('.html', '')
            ET.SubElement(item, 'link').text = article_url
            ET.SubElement(item, 'pubDate').text = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')

    # Create the XML tree from the RSS element
    tree = ET.ElementTree(rss)

    # Save the feed to a file
    tree.write(FEED_FILE, encoding='utf-8', xml_declaration=True)
    print(f"RSS Feed generated: {FEED_FILE}")

# Generate the RSS feed
if __name__ == "__main__":
    generate_rss_feed()
