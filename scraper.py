import requests
import json
from datetime import datetime

# --- CONFIGURATION ---
# Get your free key at https://developer.ticketmaster.com/
TM_API_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH"

def fetch_ticketmaster_gigs():
    """Pulls real concert data for Dublin from Ticketmaster."""
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": TM_API_KEY,
        "city": "Dublin",
        "classificationName": "music",
        "size": 100, # Number of gigs to pull
        "sort": "date,asc"
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        events = data.get('_embedded', {}).get('events', [])
        
        gigs = []
        for event in events:
            # Extract the info we need for our table
            venue_info = event.get('_embedded', {}).get('venues', [{}])[0]
            status_info = event.get('dates', {}).get('status', {}).get('code', 'N/A')
            
            # Map Ticketmaster status to our labels
            status = "Available" if status_info == "onsale" else "Sold Out"
            if status_info == "offsale": status = "N/A"

            gigs.append({
                "date": event['dates']['start']['localDate'],
                "act": event['name'],
                "venue": venue_info.get('name', 'Unknown Venue'),
                "genre": event.get('classifications', [{}])[0].get('genre', {}).get('name', 'Music'),
                "price": "Check Site", # Ticketmaster prices vary wildly/are hard to scrape
                "status": status
            })
        return gigs
    except Exception as e:
        print(f"Error fetching from Ticketmaster: {e}")
        return []

def main():
    print("Starting Dublin Gig Update...")
    all_gigs = fetch_ticketmaster_gigs()
    
    # Save the real data
    with open('gigs.json', 'w') as f:
        json.dump(all_gigs, f, indent=4)
        
    print(f"Success! Found {len(all_gigs)} real gigs in Dublin.")

if __name__ == "__main__":
    main()
