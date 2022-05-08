import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup

#webpage to scrape
jobs_page = 'https://www.ideo.com/jobs/'

#actual html of page
page = urllib2.urlopen(jobs_page)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

job_containers = soup.find_all('h2', attrs={'class': 'JobsListing--JobTitle'} )

for job_container in job_containers:
    job = job_container.text
    if 'Software' in job:
        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([job])
