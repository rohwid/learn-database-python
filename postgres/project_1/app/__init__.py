# from flask import Flask, config
from flask_restful import Api

from flask import Blueprint

from app.api.case.routes import (GatraRoutes)

blueprint = Blueprint("api", __name__)

class CustomApi(Api):
    """ Custom API Classs """
    def handle_error(self, e):
        """ Overrides the handle_error() method of the Api and adds custom error handling
        :param e: error object
        """
        code = getattr(e, 'code', 500)  # Gets code or defaults to 500
        message = getattr(e, 'message', 'Internal Server Error')
        to_dict = getattr(e, 'to_dict', None)

        # if code == 500:
        #     # capture error and send to sentry
        #     # sentry.captureException(e)
        #     data = {
        #             "status" : "ERROR",
        #             "message" : message,
        #             "data" : None
        #         }

        # handle request schema error from reqparse
        if code == 400:
            response = getattr(e, 'response', True)
            if response is None:
                # build error response
                data = {
                    "status" : "FAIL",
                    "message" : "Missing Paramater",
                    "data" : e.data['message']
                }
        if to_dict:
            data = to_dict()    

        return self.make_response(data, code)

api = CustomApi(blueprint)

#user
api.add_resource(UserRoutes, '/user')
api.add_resource(UserInfoRoutes, '/user/<user_id>')