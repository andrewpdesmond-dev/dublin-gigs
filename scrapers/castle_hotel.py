import requests
from bs4 import BeautifulSoup

def get_data():
    print("Worker: Fetching Castle Hotel Guide...")
    url = "https://www.castle-hotel.ie/event-dates/concerts-gigs/0/1"
    headers = {'User-Agent': 'Mozilla/5.0'}
    gigs = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # They list events in 'event-item' blocks
        items = soup.find_all('div', class_='event-item')
        
        for item in items:
            # Extract name and date
            name = item.find('h3').get_text(strip=True)
            date_raw = item.find('span', class_='date').get_text(strip=True)
            
            # Simple cleanup: if the venue isn't in the title, we'll label it Dublin
            venue = "Dublin Venue"
            if "at" in name.lower():
                parts = name.lower().split("at")
                venue = parts[-1].strip().title()

            gigs.append({
                "date": date_raw, 
                "act": name,
                "venue": venue,
                "genre": "Live Event",
                "price": "Check Site",
                "status": "Check Availability"
            })
    except Exception as e:
        print(f"Castle Hotel Worker Error: {e}")
        
    return gigs
