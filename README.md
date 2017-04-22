This app pulls the information from a call complaint forum and serves it in a
RESTful web service.

The app is written in Python 3.6.1 in a virtual environment

Required packages:

    - Flask             for building RESTful service
    - beautifulsoup4    for scraping HTML

To use:

    ```
    run server.py
    ```

Go to http://localhost:5000/bad_numbers to retrieve a list of all numbers.

Go to http://localhost:5000/bad_numbers?area_code={area_code} to see all the
numbers in that area code.

