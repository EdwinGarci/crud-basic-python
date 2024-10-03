from flask import Blueprint, jsonify, request

import traceback

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def index():
    try:
        return jsonify({
            'message': 'Ok',
            'success': True,
            'status': 200
        }), 200
    except Exception as ex:
        print(f"Error: {str(ex)}")
        print(f"Traceback: {traceback.format_exc()}")

        return jsonify({
            'message': "Internal Server Error", 
            'success': False
        }), 500
        