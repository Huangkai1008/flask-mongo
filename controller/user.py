from app import app
from flask import jsonify, request, abort

from models.user import User


@app.route('/api/v1/user', methods=['GET'])
def get_user():
    return jsonify(dict(user_info=User.objects.all())), 201


@app.route('/api/v1/user', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json or 'password' not in request.json:
        abort(400)
    name = request.json['name']
    password = request.json['password']

    user = User(name=name, password=password).save()
    return jsonify(dict(user=user)), 201
