from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from verify import compare_signatures

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/verify', methods=['POST'])
def verify_signature():
    if 'original' not in request.files or 'test' not in request.files:
        return jsonify({'error': 'Missing files'}), 400

    sig1 = request.files['original']
    sig2 = request.files['test']

    path1 = os.path.join(UPLOAD_FOLDER, sig1.filename)
    path2 = os.path.join(UPLOAD_FOLDER, sig2.filename)

    sig1.save(path1)
    sig2.save(path2)

    score = compare_signatures(path1, path2)

    return jsonify({'match_score': score})

@app.route('/')
def home():
    return jsonify({"message": "Signature Verification API is live"})