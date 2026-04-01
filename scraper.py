from scrapers import ticketmaster, castle_hotel, nialler9, eventbrite, entertainment, goldenplec

# ... inside main() ...
    print("--- 6/6: Fetching GoldenPlec ---")
    try: all_gigs.extend(goldenplec.get_data())
    except Exception as e: print(f"GoldenPlec Failed: {e}")
