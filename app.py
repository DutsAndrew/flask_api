from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from dotenv import load_dotenv
import json

# Import routes
from routes.api_route import api_blueprint
from routes.app_route import app_blueprint

load_dotenv()

app = Flask(__name__)
CORS(app)

# Import app after defining the routes
app.register_blueprint(api_blueprint)
app.register_blueprint(app_blueprint)

# Start server
if __name__ == "__main__":
  app.run(debug=True)