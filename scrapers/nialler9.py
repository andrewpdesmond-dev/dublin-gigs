import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_data():
    print("Worker: Fetching Nialler9...")
    url = "https://nialler9.com/gig-guide/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    gigs = []
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for the main article content where the gigs live
        content = soup.find('div', class_='entry-content') or soup.find('article')
        
        if not content:
            print("Nialler9: Could not find main content area.")
            return []

        # Nialler9 lists usually follow a 'Day' heading. 
        # We look for <li> tags that contain '@' (The Band @ Venue format)
        items = content.find_all('li')
        
        current_date = datetime.now().strftime("%Y-%m-%d")

        for item in items:
            text = item.get_text().strip()
            
            # Check for the signature "@" symbol used in his guide
            if "@" in text and len(text) < 120:
                # Split "Artist @ Venue"
                parts = text.split("@")
                act = parts[0].strip()
                
                # Handle venue and potential price in brackets: "Venue (Price)"
                venue_raw = parts[1].split("(")[0].strip()
                
                gigs.append({
                    "date": current_date, # Nialler9 is a weekly guide; we'll tag as 'current'
                    "act": act,
                    "venue": venue_raw,
                    "genre": "Indie/Alt",
                    "price": "See Nialler9",
                    "status": "Check Site"
                })

        print(f"Nialler9 Worker: Found {len(gigs)} potential gigs.")
    except Exception as e:
        print(f"Nialler9 Worker Error: {e}")
        
    return gigs
