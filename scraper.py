import requests
import json

# --- CONFIGURATION ---
# Replace the text inside the quotes with your actual Consumer Key
TM_API_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH" 

def main():
    print("Starting Ticketmaster fetch for Dublin...")
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    
    # We ask for Music in Dublin, sorted by date
    params = {
        "apikey": TM_API_KEY,
        "city": "Dublin",
        "classificationName": "music",
        "size": 100,
        "sort": "date,asc"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # This will error if your API key is wrong
        data = response.json()
        
        # Dig into the Ticketmaster data structure
        events = data.get('_embedded', {}).get('events', [])
        
        processed_gigs = []
        for event in events:
            # Extract venue name
            venues = event.get('_embedded', {}).get('venues', [{}])
            venue_name = venues[0].get('name', 'Dublin Venue')
            
            # Extract genre
            classifications = event.get('classifications', [{}])
            genre = classifications[0].get('genre', {}).get('name', 'Music')
            
            # Extract status
            status_code = event.get('dates', {}).get('status', {}).get('code', 'onsale')
            status_text = "Available" if status_code == "onsale" else "Sold Out"

            processed_gigs.append({
                "date": event['dates']['start']['localDate'],
                "act": event['name'],
                "venue": venue_name,
                "genre": genre,
                "price": "Check Ticketmaster",
                "status": status_text
            })
        
        # Save the new data
        with open('gigs.json', 'w') as f:
            json.dump(processed_gigs, f, indent=4)
        
        print(f"Success! Found {len(processed_gigs)} gigs.")

    except Exception as e:
        print(f"FAILED to fetch data. Error: {e}")
        # If it fails, we'll keep the file empty so we know it's not working
        with open('gigs.json', 'w') as f:
            json.dump([], f)

if __name__ == "__main__":
    main()
