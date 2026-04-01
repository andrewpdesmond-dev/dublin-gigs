import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    print("Worker: Fetching Nialler9...")
    url = "https://nialler9.com/gig-guide/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    gigs = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # We look for the main content area
        items = soup.find_all('li')
        for item in items:
            text = item.get_text()
            # Nialler9 format: "Band @ Venue (Price)"
            if "@" in text and len(text) < 100:
                parts = text.split("@")
                act = parts[0].strip()
                venue_part = parts[1].split("(")[0].strip()
                
                gigs.append({
                    "date": datetime.now().strftime("%Y-%m-%d"), # Defaults to today's date
                    "act": act,
                    "venue": venue_part,
                    "genre": "Indie/Alt",
                    "price": "See Nialler9",
                    "status": "Check Site"
                })
    except Exception as e:
        print(f"Nialler9 Worker Error: {e}")
        
    return gigs
