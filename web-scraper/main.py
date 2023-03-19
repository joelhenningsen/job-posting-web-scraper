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

    print("This program allows you to web scrape job posts from LinkedIn.")
    print("Please enter a job or company, then a location to scrape.")

    job_input = input('Job/Company: ')
    location_input = input('Location: ')

    url, job, location = scraper.get_url(job_input, location_input)
    job_container = scraper.get_job_container(url)
    file_name = generate_csv.write_to_csv(job_container, job, location)
    
    print(f"Your web scraped file has been exported as: '{file_name}'")
    print(f"The data was scraped from this url: {url}")


if __name__ == "__main__":
    main()