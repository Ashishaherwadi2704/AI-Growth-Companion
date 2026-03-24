import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///database.db')
    
    # AI Configuration
    DEFAULT_AI_PROVIDER = 'groq'
    MAX_MESSAGE_LENGTH = 1000
    TYPING_DELAY = 1  # seconds
    
    # Security
    BCRYPT_LOG_ROUNDS = 12
    SESSION_TIMEOUT = 3600  # 1 hour
