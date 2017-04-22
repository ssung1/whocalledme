#!Scripts/python

import unittest
from badnumber import BadNumber
import json

class TestBadNumber( unittest.TestCase ):
    def setUp( self ):
        self.sut = BadNumber(
            area_code = "987",
            phone_number = "123-765-4232",
            comment_count = 3,
            comment = "asdf"
            )
    
    def test_create_bad_number( self ):
        self.assertEqual( "987", self.sut.area_code )
        
    def test_bad_number_json_area_code( self ):
        js = json.dumps( self.sut.__dict__ )
        obj = json.loads( js )
        self.assertEqual( obj[ "area_code" ], self.sut.area_code )
        
    def test_bad_number_json_phone_number( self ):
        js = json.dumps( self.sut.__dict__ )
        obj = json.loads( js )
        self.assertEqual( obj[ "phone_number" ], self.sut.phone_number )
        

if __name__ == "__main__":
    unittest.main()        
