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
    """Main function."""

    url = scraper.get_url()
    job_container = scraper.get_job_container(url)
    generate_csv.write_to_csv(job_container)


if __name__ == "__main__":
    main()