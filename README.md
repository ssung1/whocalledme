This app pulls the information from a call complaint forum and serves it in a
RESTful web service.

The app is written in Python 3.6.1 in a virtual environment.  To
build the virtual environment in the application home directory, do

    python -m venv .

Required packages:

    Flask             for building RESTful service
    beautifulsoup4    for scraping HTML

To run:

    run server.py

Go to `http://localhost:5000/bad_numbers` to retrieve a list of all numbers.

Go to `http://localhost:5000/bad_numbers?area_code={area_code}` to see all the
numbers in that area code.

### Additional Settings

The config.py file stores settings for the application.

If use_cache is set to True, then the application will reuse the results
scraped from the web page.

If auto_refresh is set to True, then the application will periodically
scrape the results from the web page.
