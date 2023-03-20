"""linkedin_scraper.py 

Sylve Baum
Joel Henningsen
Richard Sapp

17 Mar, 2023

A web scraper that takes input from the user and searches for job \
postings on LinkedIn. User will input location and keyword for a job \
when prompted and the program will scrape LinkedIn's job listings, \
returning job titles, company names, locations, and dates posted.
"""


import requests
from bs4 import BeautifulSoup

def get_input():
    """Gets the the user's input on the job/company and the location they want 
    to scrape for on LinkedIn.
    
    Returns:
        job_input (str): A string of only alphanumeric characters or a space 
        entered by the user for the job/company they want to search.
        location_input (str): A string of only alphanumeric characters or a 
        space entered by the user for the location they want to search.
    """
    # Looping for valid inputs
    while True:
        job_input = input('Job/Company: ').lower()
        if job_input.isalnum() or " " in job_input:
            break
        else:
            print("Sorry, your input is invalid. Only alphanumeric characters "
                  "are allowed.")
    while True:
        location_input = input('Location: ').lower()
        if location_input.isalnum() or " " in location_input:
            break
        else:
            print("Sorry, your input is invalid. Only alphanumeric characters "
                  "are allowed.")
    
    return job_input, location_input


def get_url(job_input, location_input):
    """Get URL of a LinkedIn page to be scraped.
    
    Args:
        job_input (str): User-input job keyword to search on LinkedIn.
        location_input (str): User-input location keyword to search \
            on LinkedIn.

    Returns:
        url (str): LinkedIn URL to be scraped.
        job (str): The job input in a format that can be inserted into the \
            output file name.
        location (str): The location input in a format that can be inserted \
            into the output file name.
    """

    # Format user input job keyword to use for file_name
    job = job_input.strip().replace(' ', '_').replace('\\', '').replace\
        ('/', '').replace(':','').replace('*', '').replace('?', '')\
            .replace('"', '').replace('<','').replace('>','').replace('|', '')
    # Changing to file name format
    job_mod = job.replace('_', '%20')
    
    # Format user input location keyword to use for file_name
    location = location_input.strip().replace(' ', '_').replace('\\', '')\
        .replace('/', '').replace(':','').replace('*', '').replace('?', '')\
            .replace('"', '').replace('<','').replace('>','').replace('|', '')
    # Changing to URL format
    location_mod = location.replace('_', '%20')
    
    # URL of the LinkedIn page to be scraped
    url = (f'https://www.linkedin.com/jobs/search?'
        f'keywords={job_mod}&location={location_mod}')

    return url, job, location


def get_job_container(url):
    """Fetch HTML, parse with BS4, and locate job information.

    Args:
        url (str): URL of LinkedIn page to scrape

    Returns:
        job_container (str): HTML element containing job listings.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64), \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110\
                Safari/537.3'}
    # Make the request to the URL with the headers
    response = requests.get(url, headers)
    # Making an object using BeautifulSoup class
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assinging the container element where the list of jobs is located
    job_container = soup.find('section', {'class': 'two-pane-serp-page__results-list'})
    
    # If the job_container doesn't exist, check for a different class
    if job_container is None:
        job_container = soup.find('ul', {'class': 'jobs-search__results-list'})
    
    # Return result to function
    return job_container
    

def get_date_posted(job_post):
    """Check two HTML classes for date listing was posted to LinkedIn.

    Args:
        job_post (str): URL of LinkedIn page to scrape.

    Returns:
        date_posted (str): Date a job was listed on LinkedIn.
        'not found' (str): Returns 'not found' if no date found in \
            either class searched.
    """

    # First class to try
    try:
        date_posted = job_post.find\
            ('time', {'class': 'job-search-card__listdate--new'})\
                .get_text().strip()
        return date_posted

    # Go to the 'fallback class' if date_posted returns AttributeError
    except AttributeError:
        # Checking this class for a value
        try:
            date_posted = job_post.find\
                ('time', {'class': 'job-search-card__listdate'})\
                    .get_text().strip()
            return date_posted
        # If both classes fail to find data, put 'not found' instead.
        except AttributeError:
            return 'not found'


def get_info(job_container):
    """Find title, company, location, and date posted for all jobs.

    Args:
        job_container (str): HTML element containing job listings.

    Returns:
        all_jobs_info (list): List of lists each containing job \
            title, company name, location, and date posted for a job \
            listing.
    """

    # Initialize the list to store all the jobs
    all_jobs_info = []

    # Checking if job_container couldn't be found
    if job_container is None:
        print("Error: no job container found.")
        # Return an empty list
        return all_jobs_info
    
    # Iterating over all job posts and stripping the information
    for job_post in job_container.find_all\
        ('div', {'class': 'base-search-card__info'}):
        try:
            job_title = job_post.find\
                ('h3', {'class': 'base-search-card__title'})\
                    .get_text().strip()
        except AttributeError:
            return 'not found'
        
        try:
            company_name = job_post.find\
                ('h4', {'class': 'base-search-card__subtitle'})\
                    .get_text().strip()
        except AttributeError:
            return 'not found'
        
        try:
            location = job_post.find\
                ('span', {'class': 'job-search-card__location'})\
                    .get_text().strip()
        except AttributeError:
            return 'not found'
        
        try:
            date_posted = get_date_posted(job_post)
        except AttributeError:
            return 'not found'

        # Store all job info in list to be written to csv later
        all_jobs_info.append([job_title, company_name, location, date_posted])
        
    return all_jobs_info
