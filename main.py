import urllib
from datetime import date
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

#webpage to scrape
jobs_page = 'https://www.thomann.de/intl/us/harley_benton_te_62cc_lpb.htm'
# jobs_page = 'https://www.thomann.de/intl/co/harley_benton_te_20mn_bm_standard_series.htm'

#actual html of page
page = urllib.request.urlopen(jobs_page)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

title_containers = soup.find('meta', attrs={'property': 'og:title'})
availability_containers = soup.find('span', attrs={'class': 'fx-availability'} )
price_containers = soup.find('meta', attrs={'itemprop': 'price'} )
currency_containers = soup.find('meta', attrs={'itemprop': 'priceCurrency'} )

today = date.today().strftime('%d/%m/%Y')
title = title_containers["content"]
availability = availability_containers.text.strip()
price = price_containers["content"]
currency = currency_containers["content"]

result = Fore.RED + ' ' + today + Fore.WHITE + ' - ' + Fore.GREEN + title + ': ' + Fore.BLUE + availability + Fore.WHITE + ' - ' + Fore.MAGENTA + '$' + price + ' ' + currency

print(result)

with open('index.txt', 'w') as output_file:
    output_file.write(result)

