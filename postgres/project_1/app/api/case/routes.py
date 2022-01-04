"""This module does get topic gatra"""
from flask_restful import Resource

#jwt
from flask_jwt_extended import jwt_required

#serializer
from app.api.serializer import EntitySchema

#user modules
from app.api.case.modules.case import GatraServices

#config
from app.config import error

#HTTP Response
from app.api.http_response import HttpResponse

#Http error response
from app.api.error.http import BadRequest


ERROR = error.ERROR 

class GatraRoutes(Resource):

    def get(self, event_id):
        """Gatra"""
        def get(self):
            response = GatraServices.show_all()
            return response