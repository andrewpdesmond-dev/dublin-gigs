# Create this file in a folder named 'scrapers'
import requests

def get_data(api_key):
    print("Worker: Fetching Ticketmaster...")
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": api_key, 
        "city": "Dublin", 
        "classificationName": "music",
        "size": 50,
        "sort": "date,asc"
    }
    
    gigs = []
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        events = response.json().get('_embedded', {}).get('events', [])
        
        for e in events:
            gigs.append({
                "date": e['dates']['start']['localDate'],
                "act": e['name'],
                "venue": e.get('_embedded', {}).get('venues', [{}])[0].get('name', 'Dublin'),
                "genre": e.get('classifications', [{}])[0].get('genre', {}).get('name', 'Music'),
                "price": "Check Site",
                "status": "Available" if e.get('dates', {}).get('status', {}).get('code') == 'onsale' else "Sold Out"
            })
    except Exception as e:
        print(f"Ticketmaster Worker Error: {e}")
    return gigs
