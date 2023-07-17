from flask import jsonify

def index():
  return jsonify({'message': 'Welcome to the API check out the docs to get access to the correct data'})

def users():
  return jsonify({'users': ['John Doe', 'Jane Doe']})
