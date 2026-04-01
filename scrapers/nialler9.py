import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    print("Worker: Fetching Nialler9...")
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'}
    gigs = []
    
    try:
        # Step 1: Find the CURRENT gig guide link from the homepage
        home_res = requests.get("https://nialler9.com/category/gigs-festivals/dublin-gig-guide/", headers=headers, timeout=10)
        home_soup = BeautifulSoup(home_res.text, 'html.parser')
        
        # Find the first article link
        first_article = home_soup.find('h2', class_='entry-title')
        if not first_article: 
            first_article = home_soup.find('article') # Fallback
            
        target_url = first_article.find('a')['href']
        print(f"Nialler9: Target found -> {target_url}")

        # Step 2: Scrape that specific page
        res = requests.get(target_url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Look for the <li> list items that have '@'
        items = soup.find_all('li')
        for item in items:
            text = item.get_text().strip()
            if "@" in text and len(text) < 100:
                parts = text.split("@")
                gigs.append({
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "act": parts[0].strip(),
                    "venue": parts[1].split("(")[0].strip(),
                    "genre": "Indie/Alt",
                    "price": "See Nialler9",
                    "status": "Check Site"
                })
        print(f"Nialler9: Found {len(gigs)} gigs.")
    except Exception as e:
        print(f"Nialler9 Error: {e}")
        
    return gigs
