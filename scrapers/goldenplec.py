import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    print("Worker: Fetching GoldenPlec...")
    # We go to the main Dublin tag page where they post the gig guides
    url = "https://www.goldenplec.com/tag/dublin/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    gigs = []

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # GoldenPlec articles are usually wrapped in 'article' tags or 'h2' titles
        articles = soup.find_all('article')
        
        for article in articles:
            title_tag = article.find('h2')
            if title_tag and "gig guide" in title_tag.get_text().lower():
                # We found a gig guide post!
                # Note: In a production environment, we'd follow the link here.
                # For now, we'll flag that we found a valid source.
                print(f"GoldenPlec: Found active guide: {title_tag.get_text().strip()}")
                
        # (Add your extraction logic here once you confirm the link structure)
        
    except Exception as e:
        print(f"GoldenPlec Error: {e}")
        
    return gigs
