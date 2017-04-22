#!Scripts/python

import puller
from flask import Flask, jsonify, request
import config

app = Flask(__name__)

@app.route( "/v1.0/bad_numbers" )
def all_phone_numbers():
    area_code = request.args.get( "area_code" )
    if area_code != None:
        badnumber_list = []
    else:
        badnumber_list = [ x.__dict__
            for x in puller.pull_page( config.source_url ) ]
    return jsonify( badnumber_list )

if __name__ == "__main__":
    app.run( debug = True )