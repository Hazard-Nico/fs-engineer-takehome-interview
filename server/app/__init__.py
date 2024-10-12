from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from .response import post_success, bad_request, not_found, unauthorized, forbidden
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
# Create the SQLAlchemy db instance
db = SQLAlchemy(app)
CORS(app, supports_credentials=True)
migrate = Migrate(app, db)
jwt = JWTManager(app)
# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Your Flask App"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Import models
from .models.Profile import Profile


@app.route('/profile', methods=['POST'])
def post_profile():
    try:
        data = request.get_json()
        name = data.get('name')
        identity_number = data.get('identity_number')
        email = data.get('email')
        date_of_birth = data.get('date_of_birth')
        profile = Profile(name, identity_number, email, date_of_birth)
        db.session.add(profile)
        db.session.commit()
        return post_success({
            'name': profile.name,
            'identity_number': profile.identity_number,
            'email': profile.email,
            'date_of_birth': profile.date_of_birth,
        }, 'Profile created successfully')
    except Exception as e:
        print(e)
        # return bad_request({}, 'An error occurred while processing your request')

