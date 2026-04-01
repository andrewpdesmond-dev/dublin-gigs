import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    print("Worker: Fetching Eventbrite...")
    # Using the 'Music' specific sub-page
    url = "https://www.eventbrite.ie/d/ireland--dublin/music--events--this-week/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    gigs = []

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find event cards
        cards = soup.find_all('div', class_='SearchResultCard') or soup.find_all('article')
        
        for card in cards:
            title = card.find('h3')
            if title:
                name = title.get_text().strip()
                # Simple filter to keep it to music keywords
                if any(word in name.lower() for word in ['gig', 'concert', 'live', 'band', 'tour', 'dj', 'festival']):
                    gigs.append({
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "act": name,
                        "venue": "Dublin Venue (Eventbrite)",
                        "genre": "Music",
                        "price": "Check Site",
                        "status": "Available"
                    })
        print(f"Eventbrite: Found {len(gigs)} music events.")
    except Exception as e:
        print(f"Eventbrite Error: {e}")
        
    return gigs
