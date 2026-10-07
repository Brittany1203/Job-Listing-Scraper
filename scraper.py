import csv
import requests
from bs4 import BeautifulSoup

res = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(res.content, 'html.parser')

# Find ALL job card boxes on the page
job_cards = soup.find_all('div', class_='card-content')

jobs = []

for job_card in job_cards:
    job_title = job_card.find('h2', class_='title').text.strip()
    company_name = job_card.find('h3', class_='company').text.strip()
    location = job_card.find('p', class_='location').text.strip()
    job_link = job_card.find('a', string='Apply')['href']

    job = {
        'title': job_title,
        'company': company_name,
        'location': location,
        'detail_link': job_link
    }

    jobs.append(job)

csv_file = 'jobs.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'company', 'location', 'detail_link'])
    writer.writeheader()
    writer.writerows(jobs)

print(f'Successfully scraped {len(jobs)} jobs and saved to {csv_file}')