from flask import Flask, jsonify
import pytest

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping='ping')
    
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)