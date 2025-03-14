from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["news_personalization"]
users_collection = db["users"]

# Avoid circular import by importing routes at the end
from app import routes  # This should be at the bottom
