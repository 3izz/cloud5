import firebase_admin
from firebase_admin import credentials, firestore
import os

def initialize_firebase():
    try:
        # Get the absolute path to the credentials file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        cred_path = os.path.join(parent_dir, 'firebase-credentials.json')
        
        # Initialize Firebase Admin SDK with explicit configuration
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {
            'projectId': 'cloud-4cb2f',
            'storageBucket': 'cloud-4cb2f.appspot.com'
        })
        
        # Initialize Firestore
        db = firestore.client()
        return db
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return None

# Initialize Firebase when this module is imported
db = initialize_firebase() 