from bs4 import BeautifulSoup
import requests
import os

# List of URLs
urls = ["https://www.922proxy.com/meal.html"]

# Create the 'htmls' directory if it doesn't exist
# if not os.path.exists('htmls'):
#     os.makedirs('htmls')

# Loop through the URLs
for link in urls:
    r = requests.get(link)
    # Sanitize the link to create a valid filename
    filename = f"htmls/{link.split('/')[-1].replace('?', '').replace('&', '')}.html"
    
    # Write the HTML content to a file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r.text)

    print(f"Saved HTML content from {link} to {filename}")
