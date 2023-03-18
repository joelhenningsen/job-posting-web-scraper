"""generate_csv.py 

Sylve Baum
Joel Henningsen
Richard Sapp

17 Mar, 2023

This module creates headers and outputs data into a .csv file.
"""


import csv
import linkedin_scraper as scraper


def write_to_csv(job_container):
    """Write job information to a CSV file.

    Args:
        job_container (str): HTML element containing job listings.
    """

    # Opening file and writing the scraped data to it
    with open('output_job_scrape.csv', 'w', encoding="utf-8", newline='') as f:
        # Making a writer through the CSV module
        writer = csv.writer(f)
        writer.writerow(['Job Title', 'Company', 'Location', 'Date Posted'])

        # Use writer to put all scraped data into a CSV file
        for i in scraper.get_info(job_container):
            writer.writerow(i)
