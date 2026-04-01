import json
from scrapers import ticketmaster, castle_hotel, nialler9

# Replace with your actual key
TM_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH"

def deduplicate_gigs(gigs):
    """Removes duplicate entries based on Act and Date."""
    unique_gigs = []
    seen = set() # A 'set' is a fast way to track unique items
    
    for gig in gigs:
        # We create a unique "fingerprint" for each gig (e.g., "2026-04-15|Hozier")
        # We lowercase everything to make sure "Hozier" and "hozier" match
        fingerprint = f"{gig['date']}|{gig['act'].lower().strip()}"
        
        if fingerprint not in seen:
            unique_gigs.append(gig)
            seen.add(fingerprint)
        else:
            print(f"Master: Removing duplicate found for {gig['act']} on {gig['date']}")
            
    return unique_gigs

def main():
    all_gigs = []
    
    # 1. Collect from Ticketmaster
    try:
        all_gigs.extend(ticketmaster.get_data(TM_KEY))
    except Exception as e: print(f"TM Error: {e}")

    # 2. Collect from Castle Hotel
    try:
        all_gigs.extend(castle_hotel.get_data())
    except Exception as e: print(f"Castle Hotel Error: {e}")

    # 3. Collect from Nialler9
    try:
        all_gigs.extend(nialler9.get_data())
    except Exception as e: print(f"Nialler9 Error: {e}")
    
    # --- THE DE-DUPLICATOR ---
    print(f"Total raw gigs found: {len(all_gigs)}")
    clean_list = deduplicate_gigs(all_gigs)
    print(f"Final clean count: {len(clean_list)}")
    
    # 4. Save the finalized, clean list
    with open('gigs.json', 'w') as f:
        json.dump(clean_list, f, indent=4)
        
    print("--- Pipeline complete. Data is clean and saved! ---")

if __name__ == "__main__":
    main()
