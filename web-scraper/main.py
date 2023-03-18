"""main.py 

Sylve Baum
Joel Henningsen
Richard Sapp

17 Mar, 2023

Main module, initiates scraping process.
"""


import generate_csv
import linkedin_scraper as scraper


def main():
    """Main function. Calling functions from other modules."""

    url, job, location = scraper.get_url()
    job_container = scraper.get_job_container(url)
    generate_csv.write_to_csv(job_container, job, location)


if __name__ == "__main__":
    main()