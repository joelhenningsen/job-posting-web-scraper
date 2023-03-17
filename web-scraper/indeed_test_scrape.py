"""Test file to see how Indeed can be scraped."""


import requests
from bs4 import BeautifulSoup
import csv


# Creating a header to represent a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64), AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# URL of the LinkedIn page to be scraped
location = input('What location? ')
job_keyword = input('What kind of job? ')
job_keyword = job_keyword.replace(" ", "%20")
url = f'https://www.linkedin.com/jobs/search?keywords={job_keyword}&location={location}'

# Make the request to the URL with the headers
response = requests.get(url, headers=headers)

# Making an object using BeautifulSoup class
soup = BeautifulSoup(response.content, 'html.parser')

# Assinging the container element where the list of jobs is located
job_container = soup.find('section', {'class': 'two-pane-serp-page__results-list'})

# Opening file and writing the scraped data to it
with open('output/linkedin_scrape.csv', 'w', newline='') as f:
   # Making a writer through the CSV module
    writer = csv.writer(f)
    writer.writerow(['Job Title', 'Company', 'Location', 'Date Posted'])

    # Iterating over all job posts and stripping the information
    for job_post in job_container.find_all('div', {'class': 'base-search-card__info'}):
        job_title = job_post.find('h3', {'class': 'base-search-card__title'}).get_text().strip()
        company_name = job_post.find('h4', {'class': 'base-search-card__subtitle'}).get_text().strip()
        location = job_post.find('span', {'class': 'job-search-card__location'}).get_text().strip()

        # First class to try
        try:
            date_posted = job_post.find('time', {'class': 'job-search-card__listdate--new'}).get_text().strip()
        
        # Go to the 'fallback class' if date_posted returns an AttributeError
        except AttributeError:
            # Checking this class for a value
            try:
                date_posted = job_post.find('time', {'class': 'job-search-card__listdate'}).get_text().strip()
            # If both classes fail to find data, 'not found' put isntead
            except AttributeError:
                date_posted = 'not found'

        # Using the writer to put all of the scraped data into a CSV file
        writer.writerow([job_title, company_name, location, date_posted])