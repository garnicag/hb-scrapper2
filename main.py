import urllib
from datetime import date
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

#webpage to scrape
scrapeTarget = 'https://www.thomann.de/intl/search_dir.html?sw=TE-62CC&smcs=0bd321_3144'

#actual html of page
page = urllib.request.urlopen(scrapeTarget)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

table = Table(title="\n Harley Benton Availability from Thomann")

table.add_column("Date", style="red")
table.add_column("Model", style="green", no_wrap=False)
table.add_column("Color", style="yellow")
table.add_column("Availability", style="blue")
table.add_column("Price", style="magenta")

today = date.today().strftime("%d/%m/%Y")

for singleItem in soup.find_all('div', attrs={'class': 'product'}):
    title = singleItem.find(class_="title__manufacturer").text + " " + singleItem.find(class_="title__name").text.strip()
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

        availability = singleItem.find(class_="product__availability").text.strip()
        price = "$" + singleItem.find(class_="product__price-primary").text.replace("$", "").strip() + " USD"
        table.add_row(today, title, color, availability, price)

console = Console()
console.print(table)
console.print(scrapeTarget + "\n")

""" 
with open('index.txt', 'w') as output_file:
    output_file.write(result)
"""
