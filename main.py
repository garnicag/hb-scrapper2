import urllib
from datetime import date
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

#webpage to scrape
scrapeTarget = 'https://www.thomann.de/intl/search_dir.html?sw=TE-62CC&smcs=0bd321_3144'

#actual html of page
page = urllib.request.urlopen(scrapeTarget)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

for singleItem in soup.find_all('div', attrs={'class': 'product'}):
    today = Fore.RED + date.today().strftime("%d/%m/%Y")
    title = Fore.GREEN + singleItem.find(class_="title__manufacturer").text + " " + singleItem.find(class_="title__name").text.strip()
    dash = Fore.WHITE + "-"
    color = ""
    if not 'Bundle' in title:
        if 'LPB' in title:
            color = "Lake Placid Blue"
        elif 'CF' in title:
            color = "Charcoal Frost"
        elif 'IS' in title:
            color = "Inca Silver"
        elif 'SP' in title:
            color = "Shell Pink"
        elif 'DR' in title:
            color = "Dakota Red"
        elif 'SFG' in title:
            color = "Sea Foam Green"

        availability = Fore.BLUE + singleItem.find(class_="product__availability").text.strip()
        price = Fore.MAGENTA + singleItem.find(class_="product__price-primary").text.strip()
        print(today, dash, title + " (" + color + ")", dash, availability, dash, price)

""" 
with open('index.txt', 'w') as output_file:
    output_file.write(result)
 """
