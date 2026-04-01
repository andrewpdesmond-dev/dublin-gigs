import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    print("Worker: Fetching Entertainment.ie...")
    url = "https://entertainment.ie/events/listing/music/dublin/all/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    gigs = []
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Entertainment.ie lists events by day
        # Each event is usually a 'div' or 'li' within the listing area
        items = soup.find_all('div', class_='event-list-item') or soup.select('.listing-item')

        for item in items:
            title = item.find('h3')
            venue_info = item.find('p', class_='venue') # Class name might vary slightly
            
            if title:
                act_name = title.get_text(strip=True)
                venue = venue_info.get_text(strip=True) if venue_info else "Dublin Venue"
                
                gigs.append({
                    "date": datetime.now().strftime("%Y-%m-%d"), # It's a daily list
                    "act": act_name,
                    "venue": venue,
                    "genre": "Live Music",
                    "price": "See Site",
                    "status": "Available"
                })
        print(f"Entertainment.ie: Found {len(gigs)} events.")
    except Exception as e:
        print(f"Entertainment.ie Error: {e}")
        
    return gigs
