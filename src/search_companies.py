import requests
from bs4 import BeautifulSoup

def find_companies(search_query, num_pages=1):
    """Search for companies using DuckDuckGo and return their names."""
    companies = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(num_pages):
        url = f"https://duckduckgo.com/html/?q={search_query}&b={page * 50}"  # DuckDuckGo pagination uses 'b'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        #Print the raw HTML to inspect the structure (for debugging)
        print(soup.prettify())
        
        # DuckDuckGo search result links are stored in 'a' tags with the class 'result__a'
        results = soup.find_all("a", class_="result__a")
        for result in results:
            company_name = result.text.strip()
            if company_name not in companies:
                companies.append(company_name)

    return companies
