from flask import Flask
from database import db
from flask_restful import Api
from resources import routes

app = Flask(__name__)
app.config.from_object('database.db.Config')
api = Api(app)
    
db.initialize_db(app)
routes.initialize_routes(api)
