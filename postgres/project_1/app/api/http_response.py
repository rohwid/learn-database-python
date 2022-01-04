""" 
    HTTP Response
    __________
    This module to handle HTTP Success & Error code
"""
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
"""
    2xx Success
"""
class HttpResponse:
    def __init__(self, data=None, message=None):
        self.data = data
        self.message = message

        self.response = {
            "status" : None,
            "message" : self.message,
            "data" : self.data
        }


    def no_content(self):
        """
            Function to return 204 HTTP success message
        """
        return ('', 204)


    def ok(self):
        """
            Function to return 200 HTTP success message
        """
        self.response["status"] = "OK"
        return (self.response, 200)


    def created(self):
        """
            Function to return 201 HTTP success message
        """
        self.response["status"] = "OK"
        return (self.response, 201)


    def accepted(self):
        """
            Function to return 202 HTTP success message
        """
        self.response["status"] = "OK"
        return (self.response, 202)