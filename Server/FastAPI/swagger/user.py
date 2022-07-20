from flask import request
from flask_restx import Resource, Namespace, fields

import hashlib


discussion = {}
count = 1

User = Namespace(
    name="/user",
    description="User DB와의 연동을 위한 API입니다."
)


@User.route('/check-user-id')
class CheckUserId(Resource):
    @User.expect(User.model('Check User Id', {
        "userId": fields.String(required=True, description="UserId")
    }))
    def post(self):
        global count
        global discussion


@User.route('/check-email')
class CheckEmail(Resource):
    @User.expect(User.model('Check Email', {
        "email": fields.String(required=True, description="Email")
    }))
    def post(self):
        global count
        global discussion


@User.route('/register')
class Register(Resource):
    @User.expect(User.model("Register", {
        "userId": fields.String(required=True, description="UserId"),
        "password": fields.String(required=True, description="Password"),
        "email": fields.String(required=True, description="Email")
    }))
    def post(self):
        global count
        global discussion


@User.route('/login')
class Login(Resource):
    @User.expect(User.model("Login", {
        "userId": fields.String(required=True, description="UserId"),
        "password": fields.String(required=True, description="Password")
    }))
    def post(self):
        global count
        global discussion


@User.route('/auto-login/<token>')
class AutoLogin(Resource):
    def get(self):
        """토큰 값을 비교해 자동 로그인 기능을 수행합니다."""
        global count
        global discussion


@User.route('/get-user-data')
class GetUserData(Resource):
    @User.expect(User.model("GetUserData", {
        "userId": fields.String(required=True, description="UserId")
    }))
    def post(self):
        global count
        global discussion


@User.route('/update-user-data')
class UpdateUserdata(Resource):
    @User.expect(User.model("UpdateUser", {
        "userId": fields.String(required=True, description="UserId"),
        "password": fields.String(required=True, description="Password"),
        "email": fields.String(required=True, description="Email"),
        "name": fields.String(required=True, description="Name"),
        "phoneNumber": fields.String(required=True, description="PhoneNumber")
    }))
    def post(self):
        global count
        global discussion


@User.route('/delete-user')
class DeleteUser(Resource):
    @User.expect(User.model("DeleteUser", {
        "userId": fields.String(required=True, desciption="UserId")
    }))
    def post(self):
        global count
        global discussion