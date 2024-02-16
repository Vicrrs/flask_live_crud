from flask import request, jsonify, make_response
from . import app, db
from .models import User

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route successful'}), 200)

# create a user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user'}), 500)
    
# get all user
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        if len(users):
            return make_response(jsonify({'users': [user.json() for user in users]}), 200)
        return make_response(jsonify({'message': 'no user found'}), 400)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users'}), 500)

# get a user by id
@app.route('/user/<int:id>', methods=['PUT'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting user'}), 500)
    
# update user
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user update'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 400)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user'}), 500)
    
# delete a user
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting user'}), 500)
