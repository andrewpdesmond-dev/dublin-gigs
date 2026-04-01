import json
from scrapers import ticketmaster

# Replace with your key
TM_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH"

def main():
    all_gigs = []
    
    # 1. Run Ticketmaster
    tm_gigs = ticketmaster.get_data(TM_KEY)
    all_gigs.extend(tm_gigs)
    
    # 2. You can add more later:
    # all_gigs.extend(castle_hotel.get_data())
    
    # 3. Save
    with open('gigs.json', 'w') as f:
        json.dump(all_gigs, f, indent=4)
        
    print(f"Pipeline complete. Total gigs: {len(all_gigs)}")

if __name__ == "__main__":
    main()
