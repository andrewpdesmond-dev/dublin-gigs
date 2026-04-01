import json
# Import the new worker too
from scrapers import ticketmaster, castle_hotel, nialler9

TM_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH"

def main():
    all_gigs = []
    
    # 1. Ticketmaster
    try:
        all_gigs.extend(ticketmaster.get_data(TM_KEY))
    except Exception as e: print(f"TM Error: {e}")

    # 2. Castle Hotel
    try:
        all_gigs.extend(castle_hotel.get_data())
    except Exception as e: print(f"Castle Hotel Error: {e}")

    # 3. Nialler9
    try:
        all_gigs.extend(nialler9.get_data())
    except Exception as e: print(f"Nialler9 Error: {e}")
    
    # Save results
    with open('gigs.json', 'w') as f:
        json.dump(all_gigs, f, indent=4)
        
    print(f"Pipeline complete. Total gigs found: {len(all_gigs)}")

if __name__ == "__main__":
    main()
