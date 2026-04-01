import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    print("Worker: Fetching Nialler9...")
    # We try the main guide first
    base_url = "https://nialler9.com/gig-guide/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    gigs = []
    
    try:
        response = requests.get(base_url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for list items with the '@' symbol
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
        
        if not gigs:
            print("Nialler9: Found 0 gigs. He might have moved the guide to a new URL.")
        else:
            print(f"Nialler9: Successfully found {len(gigs)} gigs!")

    except Exception as e:
        print(f"Nialler9 Error: {e}")
        
    return gigs
