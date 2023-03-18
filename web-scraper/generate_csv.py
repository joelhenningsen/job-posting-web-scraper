"""generate_csv.py 

Sylve Baum
Joel Henningsen
Richard Sapp

17 Mar, 2023

This module creates headers and outputs data into a .csv file.
"""


import csv
import linkedin_scraper as scraper


def write_to_csv(job_container, job, location):
    """Write job information to a CSV file.

    Args:
        job_container (str): HTML element containing job listings.
        job (str): The job input in a format that can be inserted into the output 
            file name.
        location (str): The location input in a format that can be inserted 
            into the output file name.
    """

    # Opening file and writing the scraped data to it
    filename = f"{job}_{location}_scrape.csv"
    with open(filename, 'w', encoding="utf-8", newline='') as f:
        # Making a writer through the CSV module
        writer = csv.writer(f)
        writer.writerow(['Job Title', 'Company', 'Location', 'Date Posted'])

        # Use writer to put all scraped data into a CSV file
        for i in scraper.get_info(job_container):
            writer.writerow(i)
