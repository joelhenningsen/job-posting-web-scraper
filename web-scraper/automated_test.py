"""automated_test.py 

Sylve Baum
Joel Henningsen
Richard Sapp

17 Mar, 2023

This module is an automated example of our program for testing use.
"""


import generate_csv
import linkedin_scraper as scraper


def testing(job_input, location_input):
    """Perform a scrape using pre-selected job and location inputs.
    
    Args:
        job_input (str): Job keyword to search on LinkedIn.
        location_input (str): Location keyword to search on LinkedIn.
    """
    
    print(f"Automated example.\nJob: {job_input}\nLocation: {location_input}")

    url, job, location = scraper.get_url(job_input, location_input)
    job_container = scraper.get_job_container(url)
    file_name = generate_csv.write_to_csv(job_container, job, location)

    print(f"Your web scraped file has been exported as: '{file_name}'")
    print(f"The data was scraped from this url: {url}\n")

def main():
    """Main function."""

    testing('software developer', 'portland or')
    testing('retail', 'oregon')
    testing('accountant', 'mexico')
    testing('','korea')
    testing('dogwalker','')
    testing('','')
    testing('/','')
    testing('\\', '')
    testing(':','')
    testing('*', '')
    testing('?','')
    testing('"','')
    testing('<','')
    testing('>','')
    testing('|', '')
    testing('Chegg','San Fransisco')
    
if __name__ == "__main__":
    main()
