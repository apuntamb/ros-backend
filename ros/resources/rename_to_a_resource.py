"""To structure the app using Blueprints, created this standard resources directory"""
from flask import Response, request
from models import rename_to_first_model
from flask_restful import Resource

class MyApi(Resource):
    def get(self):
        """return"""
    
    def post(self):
        """return"""

class SomeOtherApi(Resource):
    """Define the http methods"""