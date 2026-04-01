# At the top of scraper.py
from scrapers import ticketmaster, castle_hotel, nialler9, eventbrite, entertainment

# Inside the main() function
print("--- 5/5: Fetching Entertainment.ie ---")
try:
    all_gigs.extend(entertainment.get_data())
except Exception as e: 
    print(f"Entertainment.ie Failed: {e}")
