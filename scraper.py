import json
# Import both workers
from scrapers import ticketmaster, castle_hotel

# Replace with your actual key
TM_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH"

def main():
    all_gigs = []
    
    # 1. Run Ticketmaster Worker
    print("--- Starting Ticketmaster ---")
    try:
        tm_data = ticketmaster.get_data(TM_KEY)
        all_gigs.extend(tm_data)
    except Exception as e:
        print(f"Master: Ticketmaster failed: {e}")

    # 2. Run Castle Hotel Worker
    print("--- Starting Castle Hotel ---")
    try:
        castle_data = castle_hotel.get_data()
        all_gigs.extend(castle_data)
    except Exception as e:
        print(f"Master: Castle Hotel failed: {e}")
    
    # 3. Save the combined results
    with open('gigs.json', 'w') as f:
        json.dump(all_gigs, f, indent=4)
        
    print(f"--- Pipeline complete. Total gigs found: {len(all_gigs)} ---")

if __name__ == "__main__":
    main()
