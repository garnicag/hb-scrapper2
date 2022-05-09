import urllib
from datetime import date, timedelta
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
import os

#webpage to scrape
scrapeTarget = 'https://www.thomann.de/intl/search_dir.html?sw=Harley%20Benton%20TE-62&smcs=0bd321_3144'
scrapeTarget = 'https://www.thomann.de/intl/search_dir.html?smcs=0bd321_2481&oa=prd&sw=Harley%20Benton%20TE%20-bundle%20-case%20-parts%20-lh&filter=true&ls=100'
shipment = 63
currency = "COP"
rows = 0

#actual html of page
page = urllib.request.urlopen(scrapeTarget)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

table = Table(title="\n Harley Benton availability from Thomann")

table.add_column("Date", style="red")
table.add_column("Model", style="green", no_wrap=False)
table.add_column("Color", style="yellow")
table.add_column("Availability", style="blue")
table.add_column("Price + Sh", style="magenta")

today = date.today()
deliveryDateMin = today + timedelta(days=12)
deliveryDateMax = today + timedelta(days=17)
deliveryDateMin = deliveryDateMin.strftime("%a %d/%m/%Y")
deliveryDateMax = deliveryDateMax.strftime("%a %d/%m/%Y")
today = today.strftime("%d/%m/%Y")

for singleItem in soup.find_all('div', attrs={'class': 'product'}):
    title = singleItem.find(class_="title__manufacturer").text + " " + singleItem.find(class_="title__name").text.strip()
    color = ""
    rows = rows+1

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
        elif 'BK' in title:
            color = "Black High Gloss"
        elif 'CAR' in title:
            color = "Candy Apple Red"

        availability = singleItem.find(class_="product__availability").text.strip()
        price = singleItem.find(class_="product__price-primary").text.replace("$", "").replace(",", ".").strip()
        price = float(price) + shipment

        if currency == "COP":
            price = os.popen("forx -q " + str(price) + " usd cop").read().replace("$", "").replace(",", "").strip()
        
        price = round(float(price))
        price = "$" + str(price) + " " + currency
        table.add_row(today, title, color, availability, price)

console = Console()
console.print(table)
console.print(str(rows) + " results - Delivery between " + deliveryDateMin + " and " + deliveryDateMax)
console.print(scrapeTarget + "\n")

""" 
with open('index.txt', 'w') as output_file:
    output_file.write(result)
"""
