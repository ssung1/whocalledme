#!Scripts/python

import badnumber
from bs4 import BeautifulSoup
import re
import urllib.request

def pull_page( url ):
    response = urllib.request.urlopen( url )
    data = response.read()
    text = data.decode( 'utf-8' )
    return find_bad_number_list( text )

def find_previews( html_str ):
    "previews is the section that holds all the"
    "phone numbers and comments"
    soup = BeautifulSoup( html_str, "html.parser" )
    return soup.find_all( name = "ul", id = "previews" )

def find_item_list( previews ):
    return previews.find_all(
        attrs = { "class": "oos_listItem" } )

def find_item_preview_main( item ):
    return item.div.find_all(
        name = "div", attrs = { "class": "oos_previewMain" } )[0]

def find_count( item ):
    return item.div.span.string.strip()

def find_phone_number( item ):
    div_main = find_item_preview_main( item )
    return div_main.h4.a.string.strip()

def find_area_code( item ):
    div_main = find_item_preview_main( item )
    area_code_string = div_main.div.span.span.a.string.strip()
    # find the first nu
    number_part = re.findall( "\d\d\d", area_code_string )[0]
    return number_part

def find_comment( item ):
    div_body = item.div.find_all( name = "div",
        attrs = { "class": "oos_previewBody" } )[0]

    str = list( div_body.stripped_strings )
    return str[0]

def find_bad_number_list( html_str ):
    preview = find_previews( html_str )[0]
    item_list = find_item_list( preview )

    result = []
    for i in item_list:
        count = int( find_count( i ) )
        phone_number = find_phone_number( i )
        area_code = find_area_code( i )
        comment = find_comment( i )

        bn = badnumber.BadNumber(
            area_code = area_code,
            phone_number = phone_number,
            comment_count = count,
            comment = comment )

        result.append( bn )
    return result

