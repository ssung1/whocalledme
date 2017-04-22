#!Scripts/python

import puller
from flask import Flask, jsonify
import config

app = Flask(__name__)

@app.route( "/bad_numbers" )
def all_phone_numbers():
    badnumber_list = [ x.__dict__ 
        for x in puller.pull_page( config.source_url ) ]
    return jsonify( badnumber_list )
    
    
if __name__ == "__main__":
    app.run( debug = True )