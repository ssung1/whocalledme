#!Scripts/python

from flask import Flask, jsonify, request
import config
import database

app = Flask(__name__)

@app.route( "/v1.0/bad_numbers" )
def all_phone_numbers():
    area_code = request.args.get( "area_code" )
    if area_code != None:
        badnumber_list = database.find_by_area_code( area_code )
    else:
        badnumber_list = database.find_all()

    badnumber_dict = [ x.__dict__ for x in badnumber_list ]
    return jsonify( badnumber_dict )

if __name__ == "__main__":
    if config.auto_refresh:
        database.start_background_refresh()
        app.run( debug = False )
    else:
        app.run( debug = True )
