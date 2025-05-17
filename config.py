import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Firebase configuration
    FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS') or 'firebase-credentials.json'
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Security headers
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'your-salt-here'
    
    # CORS configuration
    CORS_HEADERS = 'Content-Type'
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    
    # Link Classification Settings
    SAFE_DOMAINS = ['github.com', 'stackoverflow.com', 'python.org', 'docs.python.org']
    UNSAFE_DOMAINS = ['malicious-site.com', 'scam-site.com']
    
    # Background Music Settings
    MUSIC_FILES = {
        'calm': 'static/music/calm.mp3',
        'focus': 'static/music/focus.mp3',
        'nature': 'static/music/nature.mp3'
    } 