"""generate_csv.py 

Sylve Baum
Joel Henningsen
Richard Sapp

17 Mar, 2023

This module creates headers and outputs data into a .csv file.
"""


import csv
import linkedin_scraper as scraper
from pathlib import Path


def write_to_csv(job_container, job, location):
    """Write job information to a CSV file.

    Args:
        job_container (str): HTML element containing job listings.
        job (str): The job input in a format that can be inserted into the output 
            file name.
        location (str): The location input in a format that can be inserted 
            into the output file name.
    """
    # Creating a file path
    output_dir = Path('output')
    file_name = output_dir / f"{job}_{location}_scrape.csv"

    # Create the output directory if it doesn't already exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Opening file and writing the scraped data to it
    with open(file_name, 'w', encoding="utf-8", newline='') as f:
        # Making a writer through the CSV module
        writer = csv.writer(f)
        writer.writerow(['Job Title', 'Company', 'Location', 'Date Posted'])

        # Use writer to put all scraped data into a CSV file
        for i in scraper.get_info(job_container):
            writer.writerow(i)

    return file_name
