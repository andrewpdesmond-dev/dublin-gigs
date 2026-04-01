import json
import requests
from bs4 import BeautifulSoup

def scrape_local_guide():
    """
    Example of how you might scrape a smaller, local blog or guide 
    using BeautifulSoup. (HTML structure varies wildly per site!)
    """
    gigs = []
    # Mock data representing what BeautifulSoup would extract
    gigs.append({
        "date": "2026-04-12",
        "act": "Fontaines D.C.",
        "venue": "Vicar Street",
        "genre": "Post-Punk",
        "price": "€45.00",
        "status": "Sold Out"
    })
    return gigs

def fetch_ticketmaster_api():
    """
    Example of using an API. You can get a free key at developer.ticketmaster.com
    Uncomment the code below once you have a key!
    """
    gigs = []
    # api_key = "YOUR_API_KEY_HERE"
    # url = f"https://app.ticketmaster.com/discovery/v2/events.json?city=Dublin&apikey={api_key}"
    # response = requests.get(url).json()
    # for event in response.get('_embedded', {}).get('events', []):
    #     gigs.append({
    #         "date": event['dates']['start']['localDate'],
    #         "act": event['name'],
    #         "venue": event['_embedded']['venues'][0]['name'],
    #         "genre": "N/A", # Needs deeper parsing depending on event
    #         "price": "N/A", 
    #         "status": "Available"
    #     })
    
    # Mock data to keep the site functioning while you develop
    gigs.append({
        "date": "2026-04-15",
        "act": "Hozier",
        "venue": "3Arena",
        "genre": "Indie Rock",
        "price": "€60.00",
        "status": "Available"
    })
    return gigs

def main():
    all_gigs = []
    
    # Gather data from all your sources
    all_gigs.extend(scrape_local_guide())
    all_gigs.extend(fetch_ticketmaster_api())
    
    # Save everything to a single file that index.html can read
    with open('gigs.json', 'w') as f:
        json.dump(all_gigs, f, indent=4)
    print(f"Successfully saved {len(all_gigs)} gigs to gigs.json")

if __name__ == "__main__":
    main()
