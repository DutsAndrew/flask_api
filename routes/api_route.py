# routes/api_route.py
from flask import Blueprint
from controllers import api_controller

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Use the function names directly as the view functions for the routes
api_blueprint.route('/', methods=['GET'])(api_controller.index)
api_blueprint.route('/users', methods=['GET'])(api_controller.users)