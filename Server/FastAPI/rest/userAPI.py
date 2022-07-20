from flask import request, jsonify
from flask import Blueprint
from db import db

userApi = Blueprint("user", __name__)


@userApi.route('/check-user-id', methods=['POST'])
def post_checkUserId():
    param = request.get_json()
    result = db.checkUserId(param)

    return jsonify(result)


@userApi.route('/check-email', methods=['POST'])
def post_checkEmail():
    param = request.get_json()
    result = db.checkEmail(param)

    return jsonify(result)


@userApi.route('/register', methods=['POST'])
def post_register():
    param = request.get_json()
    result = db.register(param)

    return jsonify(result)


@userApi.route('/login', methods=['POST'])
def post_login():
    param = request.get_json()
    result = db.login(param)

    return jsonify(result)


@userApi.route('/auto-login')
def post_autoLogin():
    param = request.cookies.get('token')
    result = db.autoLogin(param)

    return jsonify(result)


@userApi.route('/get-user-data', methods=['POST'])
def post_getUserData():
    param = request.get_json()
    result = db.getUserData(param)

    return jsonify(result)


@userApi.route('/update-user-data', methods=['POST'])
def post_updateUserData():
    param = request.get_json()
    result = db.updateUserData(param)

    return jsonify(result)


@userApi.route('/delete-user', methods=['POST'])
def post_deleteUser():
    param = request.get_json()
    result = db.deleteUser(param)

    return jsonify(result)
