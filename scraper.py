import json
from scrapers import ticketmaster, castle_hotel, nialler9, eventbrite, entertainment, goldenplec

# Use your actual key here
TM_KEY = "YOUR_API_KEY_HERE"

def deduplicate_gigs(gigs):
    unique_gigs = []
    seen = set()
    for gig in gigs:
        # Create a unique ID using date and a cleaned version of the act name
        fingerprint = f"{gig['date']}|{gig['act'].lower().strip()}"
        if fingerprint not in seen:
            unique_gigs.append(gig)
            seen.add(fingerprint)
    return unique_gigs

def main():
    all_gigs = []
    
    print("--- 1/6: Fetching Ticketmaster ---")
    try:
        all_gigs.extend(ticketmaster.get_data(TM_KEY))
    except Exception as e: print(f"TM Failed: {e}")

    print("--- 2/6: Fetching Eventbrite ---")
    try:
        all_gigs.extend(eventbrite.get_data())
    except Exception as e: print(f"Eventbrite Failed: {e}")

    print("--- 3/6: Fetching Nialler9 ---")
    try:
        all_gigs.extend(nialler9.get_data())
    except Exception as e: print(f"Nialler9 Failed: {e}")

    print("--- 4/6: Fetching Castle Hotel ---")
    try:
        all_gigs.extend(castle_hotel.get_data())
    except Exception as e: print(f"Castle Hotel Failed: {e}")

    print("--- 5/6: Fetching Entertainment.ie ---")
    try:
        all_gigs.extend(entertainment.get_data())
    except Exception as e: print(f"Entertainment Failed: {e}")

    print("--- 6/6: Fetching GoldenPlec ---")
    try:
        all_gigs.extend(goldenplec.get_data())
    except Exception as e: print(f"GoldenPlec Failed: {e}")

    # Clean the data
    clean_list = deduplicate_gigs(all_gigs)

    # Save to file
    with open('gigs.json', 'w') as f:
        json.dump(clean_list, f, indent=4)
        
    print(f"Done! Saved {len(clean_list)} unique gigs.")

if __name__ == "__main__":
    main()
