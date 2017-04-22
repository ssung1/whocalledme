#!Scripts/python

import badnumber
from bs4 import BeautifulSoup

def pull_page( url ):
    return [ badnumber.BadNumber( "a", "b", 3, "c" ) ]
    
def find_previews( html_str ):
    "previews is the section that holds all the"
    "phone numbers and comments"
    soup = BeautifulSoup( html_str, "html.parser" )
    return soup.find_all( name = "ul", id = "previews" )
    
def find_list_items( previews ):
    return previews.find_all(
        attrs = { "class": "oos_listItem" } )
    