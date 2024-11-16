import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin

def scrape_career_pages(companies):
    """Scrape job listings from each company's career page."""
    headers = {"User-Agent": "Mozilla/5.0"}
    job_data = []

    for company in companies:
        try:
            print(f"Scraping jobs for {company}...")
            search_query = f"{company} careers site:.in"
            google_url = f"https://www.google.com/search?q={search_query}"

            # Make request to Google search
            response = requests.get(google_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all links in the Google search result page
            search_results = soup.find_all("a", href=True)

            # Find the career page link (typically the first one in search results)
            career_page_url = None
            for link in search_results:
                href = link['href']
                # Look for a link that likely points to a career page (basic heuristic)
                if 'career' in href.lower() or 'jobs' in href.lower():
                    career_page_url = href
                    break

            if not career_page_url:
                print(f"No career page found for {company}.")
                continue

            # If the URL is relative, convert it to absolute
            if career_page_url.startswith('/'):
                career_page_url = urljoin('https://www.google.com', career_page_url)

            print(f"Found career page: {career_page_url}")

            # Fetch jobs from the career page
            response = requests.get(career_page_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            # Example: Scrape job titles, locations, and descriptions (adjust selectors)
            jobs = soup.find_all("div", class_="job-listing")  # Update this according to actual job listings' HTML structure
            for job in jobs:
                title = job.find("h2").text.strip() if job.find("h2") else "No title"
                location = job.find("span", class_="location").text.strip() if job.find("span", class_="location") else "No location"
                description = job.find("p", class_="description").text.strip() if job.find("p", class_="description") else "No description"

                job_data.append({
                    "Company": company,
                    "Title": title,
                    "Location": location,
                    "Description": description,
                    "Apply Link": career_page_url,
                })

            # Random delay between requests to avoid being blocked
            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print(f"Error scraping {company}: {e}")

    return job_data
