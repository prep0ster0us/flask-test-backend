from flask import Flask, jsonify, request
from mongo import *

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Render!"})

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route("/users", methods=["GET"])
def get_users():
    try:
        result = get_all_users()
        return jsonify(result), 200
    except LookupError:
        return jsonify({"error": "couldn't fetch users"}), 404
    
# @app.route("/users", methods=["PUT"])
# def add_user():
#     user_data = request.get_json()
#     try:
#         result = get_all_users()
#         return jsonify(result), 200
#     except LookupError:
#         return jsonify({"error": "couldn't fetch users"}), 404


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=10000)  # Use 0.0.0.0 for Render