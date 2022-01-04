"""
	Base Error handler
    NOT INTENDED TO USE DIRECTLY
"""
class BaseError(Exception):
    """ base error class """
    def __init__(self, code, message, data):
        super().__init__(code, message, data)
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        """
	        Call this in the the error handler to serialize the
	        error for the json-encoded http response body.
        """
        error_response = {
            "status"  : "FAIL",
            "message" : self.message,
            "data"    : self.data
        }

        return error_response

class BadRequest(BaseError):
    """ base http error class for any bad request"""
    def __init__(self, message=None, data=None):
        super(BaseError, self).__init__(message, data)
        self.code = 400

        self.message = message
        self.data = data

class RequestNotFound(BaseError):
    """ base http error class for any resource not found"""
    def __init__(self, message=None,data =None):
        super(BaseError, self).__init__(message, data)
        self.code = 404

        self.message = message
        self.data = data

class UnprocessableEntity(BaseError):
    """ base http error class for any resource not found"""
    def __init__(self, message=None, data=None):
        super(BaseError, self).__init__(message, data)
        self.code = 422

        self.message = message
        self.data = data

class Unauthorized(BaseError):
    """ base http error class for unauthorized access"""
    def __init__(self, message=None, data=None):
        super(BaseError, self).__init__(message, data)
        self.code = 401

        self.message = message
        self.data = data

class InsufficientScope(BaseError):
    """ base http error class for insufficient scope """
    def __init__(self, message=None, data=None):
        super(BaseError, self).__init__(message, data)
        self.code = 403

        self.message = message
        self.data = data