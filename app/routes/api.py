from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required, current_user
import random
from google.cloud import firestore

bp = Blueprint('api', __name__, url_prefix='/api')

# Simple chatbot responses
CHATBOT_RESPONSES = {
    'hello': 'Hello! How can I help you today?',
    'help': 'I can help you manage your links, play background music, or answer questions about the application.',
    'music': 'You can select background music from the music player in your dashboard.',
    'links': 'You can add, delete, and organize your links in your dashboard.',
    'default': 'I\'m not sure I understand. Try asking about links, music, or type "help" for more options.'
}

@bp.route('/chatbot', methods=['POST'])
@login_required
def chatbot():
    message = request.json.get('message', '').lower()
    
    # Simple keyword matching
    response = CHATBOT_RESPONSES['default']
    for key in CHATBOT_RESPONSES:
        if key in message:
            response = CHATBOT_RESPONSES[key]
            break
    
    return jsonify({
        'response': response
    })

@bp.route('/music/list', methods=['GET'])
@login_required
def get_music_list():
    # In a real application, this would come from a database or file system
    music_list = [
        {'id': 'calm', 'name': 'Calm Meditation', 'file': 'calm.mp3'},
        {'id': 'focus', 'name': 'Focus Music', 'file': 'focus.mp3'},
        {'id': 'nature', 'name': 'Nature Sounds', 'file': 'nature.mp3'}
    ]
    return jsonify(music_list)

@bp.route('/music/play/<music_id>', methods=['POST'])
@login_required
def play_music(music_id):
    # In a real application, this would handle music playback
    return jsonify({
        'status': 'success',
        'message': f'Playing {music_id}'
    })

@bp.route('/test-firebase')
def test_firebase():
    try:
        # Get Firebase instance
        db = current_app.firebase_db
        
        # Try to add a test document
        test_data = {
            'message': 'Firebase connection successful!',
            'timestamp': firestore.SERVER_TIMESTAMP
        }
        
        # Add to a test collection
        db.collection('test').add(test_data)
        
        return jsonify({
            'status': 'success',
            'message': 'Firebase connection is working!'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Firebase error: {str(e)}'
        }), 500 