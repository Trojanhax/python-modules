import os
from bs4 import BeautifulSoup

for file in os.listdir("htmls"):
    with open(f"htmls/{file}", 'r', encoding='utf-8') as f:
        htmlcon = f.read()
        soup = BeautifulSoup(htmlcon, "html.parser")
        print(soup.p)
        for link in soup.find_all("img"):
            # print(link)
            if link:
                href = link.get('href')  # Get the 'href' attribute value
                print(href)
            else:
                print("No <a> element found.")
