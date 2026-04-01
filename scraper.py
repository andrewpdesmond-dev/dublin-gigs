import json
# Import all your workers
from scrapers import ticketmaster, castle_hotel, nialler9, eventbrite

# Replace with your actual key
TM_KEY = "V7HypVGyprpKkeRrOV3WMO1B6NqMgEpH"

def deduplicate_gigs(gigs):
    """
    Cleans the list by removing duplicates.
    It looks at the Date and a 'Cleaned' version of the Artist name.
    """
    unique_gigs = []
    seen_fingerprints = set()
    
    print(f"Master: Starting deduplication on {len(gigs)} raw entries...")

    for gig in gigs:
        # 1. Clean the name: lowercase, remove "The ", and strip whitespace
        # This ensures "The Wolfe Tones" and "Wolfe Tones" are seen as the same
        clean_act = gig['act'].lower().replace("the ", "").strip()
        
        # 2. Create a unique fingerprint (Date + Cleaned Act)
        fingerprint = f"{gig['date']}|{clean_act}"
        
        if fingerprint not in seen_fingerprints:
            unique_gigs.append(gig)
            seen_fingerprints.add(fingerprint)
        else:
            # This is a duplicate, we skip it
            continue
            
    return unique_gigs

def main():
    all_gigs = []
    
    # --- 1. DATA COLLECTION PHASE ---
    
    print("--- 1/4: Fetching Ticketmaster ---")
    try:
        all_gigs.extend(ticketmaster.get_data(TM_KEY))
    except Exception as e: print(f"Ticketmaster Error: {e}")

    print("--- 2/4: Fetching Eventbrite ---")
    try:
        all_gigs.extend(eventbrite.get_data())
    except Exception as e: print(f"Eventbrite Error: {e}")

    print("--- 3/4: Fetching Castle Hotel ---")
    try:
        all_gigs.extend(castle_hotel.get_data())
    except Exception as e: print(f"Castle Hotel Error: {e}")

    print("--- 4/4: Fetching Nialler9 ---")
    try:
        all_gigs.extend(nialler9.get_data())
    except Exception as e: print(f"Nialler9 Error: {e}")

    # --- 2. CLEANING PHASE ---
    
    final_list = deduplicate_gigs(all_gigs)
    
    # --- 3. STORAGE PHASE ---
    
    with open('gigs.json', 'w') as f:
        json.dump(final_list, f, indent=4)
        
    print(f"SUCCESS: {len(final_list)} unique gigs saved to gigs.json")

if __name__ == "__main__":
    main()
