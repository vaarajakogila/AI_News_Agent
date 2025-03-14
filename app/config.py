import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GNEWS_API_KEY=os.getenv("GNEWS_API_KEY")
# SMTP Configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default to 587 if not found
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
