from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the API check out the docs to get access to the correct data'})

@api_blueprint.route('/users', methods=['GET'])
def users():
  return jsonify({'users': ['John Doe', 'Jane Doe']})
