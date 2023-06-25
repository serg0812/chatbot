# appweb.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import gpt4web

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json['query']
    response = gpt4web.generate_response(query)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(port=5000)
