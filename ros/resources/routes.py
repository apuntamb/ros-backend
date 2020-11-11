"""Importing model here as it's required for db creation in app.py and app.py has imported routes already <can change>"""
from models import rename_to_first_model
from .rename_to_a_resource import MyApi, SomeOtherApi

def initialize_routes(api):
    api.add_resource(MyApi, '/api/my')
    api.add_resource(SomeOtherApi, '/api/someother/<id>')
