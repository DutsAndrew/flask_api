from flask import Blueprint, jsonify

app_blueprint = Blueprint('app', __name__)

@app_blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'This is an API endpoint'})