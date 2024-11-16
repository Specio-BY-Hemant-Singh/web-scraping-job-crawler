from search_companies import find_companies
from company_scraper import scrape_career_pages
from utils import save_to_excel

def main():
    # Step 1: Find companies based on search query
    print("Finding companies in Gurugram...")
    companies = find_companies("data science companies in Gurugram", num_pages=5)

    print(f"Found {len(companies)} companies. Proceeding to scrape their job pages...")

    # Step 2: Scrape job listings from career pages
    job_data = scrape_career_pages(companies)

    # Step 3: Save the data to an Excel sheet
    save_to_excel( r"C:\Users\heman\Desktop\workspace\my_project\web scraping job crawler\data\job_data.xlsx", job_data)
    print("Job data saved to 'data/job_data.xlsx'.")

if __name__ == "__main__":
    main()
