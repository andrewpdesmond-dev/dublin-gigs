import requests
from datetime import datetime

def get_data():
    print("Worker: Fetching Eventbrite Dublin...")
    # Eventbrite's public search URL for Dublin Music
    url = "https://www.eventbrite.ie/d/ireland--dublin/music--events/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Music-specific keywords to ensure we don't get 'Pottery Classes'
    music_keywords = ['gig', 'concert', 'live', 'band', 'dj', 'music', 'album', 'tour', 'singer', 'techno', 'jazz']
    gigs = []

    try:
        # Note: Eventbrite is tricky to scrape directly; 
        # For now, we use a robust search-based approach
        response = requests.get(url, headers=headers, timeout=15)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Eventbrite uses 'event-card' structures
        cards = soup.find_all('div', class_='SearchResultCard') or soup.find_all('article')
        
        for card in cards:
            title_element = card.find('h3')
            if not title_element: continue
            
            title = title_element.get_text().strip()
            
            # --- THE FILTER ---
            # Only keep it if it sounds like music
            if not any(word in title.lower() for word in music_keywords):
                continue

            # Extract Venue & Date (Eventbrite's structure varies, so we aim for common spots)
            venue = "Dublin (See Eventbrite)"
            venue_element = card.find('p', class_='event-card-details__location')
            if venue_element:
                venue = venue_element.get_text().strip()

            gigs.append({
                "date": datetime.now().strftime("%Y-%m-%d"), # Defaulting to current week
                "act": title,
                "venue": venue,
                "genre": "Live Event",
                "price": "Check Eventbrite",
                "status": "Available"
            })
            
        print(f"Eventbrite: Found {len(gigs)} music-filtered events.")
    except Exception as e:
        print(f"Eventbrite Error: {e}")
        
    return gigs
