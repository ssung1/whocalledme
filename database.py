#!Scripts/python

import time
import threading
import puller
import config

# simulates storage into database, so we don't have to scrape
# each time the web service is called
initialized = False
all_the_bad_numbers = []
auto_refresh = True

def get_all_the_bad_numbers():
    global initialized
    global all_the_bad_numbers
    if not initialized or not config.use_cache:
        print( "scraping..." )
        refresh()
    else:
        print( "reusing cached..." )

    return all_the_bad_numbers

def refresh():
    global all_the_bad_numbers
    global initialized
    all_the_bad_numbers = []
    pulled = puller.pull_page( config.source_url )
    all_the_bad_numbers += pulled
    initialized = True

def store( bn ):
    global all_the_bad_numbers
    all_the_bad_numbers.append( bn )

def find_all():
    return get_all_the_bad_numbers()

def find_by_area_code( area_code ):
    return [x for x in get_all_the_bad_numbers()
        if x.area_code == area_code]

def background_refresh():
    global auto_refresh
    while auto_refresh:
        print( "auto_refreshing source page..." )
        refresh()
        time.sleep( 15 )

def start_background_refresh():
    refresh_thread = threading.Thread( target = background_refresh )
    refresh_thread.start()
