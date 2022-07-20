from db.connection import dbConnectionDAO as connDao
from db.user import registerDAO as regDao
from db.user import loginDAO as loginDao
from db.user import myPageDAO as mpDao

import jwt
import hashlib


# 아이디 중복 체크 (입력 중)
def checkUserId(idData):
    db = connDao.getDb('Wiki')

    if regDao.checkUserId(db, idData['userId']):
        return {'result': 'success'}
    else:
        return {'result': 'fail'}


# 이메일 중복 체크 (입력 중)
def checkEmail(emailData):
    db = connDao.getDb('Wiki')
    if regDao.checkEmail(db, emailData['email']):
        return {'result': 'success'}
    else:
        return {'result': 'fail'}


# 회원가입 처리
def register(userInfo):
    examData = {"userId": "", "password": "", "email": ""}
    if userInfo.keys() != examData.keys():
        return {'result': 'fail2'}
    else:
        db = connDao.getDb('Wiki')
        if not regDao.checkEmail(db, userInfo['email']) and not regDao.checkUserId(db, userInfo['userId']):
            regDao.addUser(db, userInfo)

            return {'result': 'success'}
        else:
            return {'result': 'fail'}


# 로그인 처리
def login(loginData):
    examData = {"userId": "", "password": ""}
    if loginData.keys() != examData.keys():
        return {'result': 'fail'}
    else:
        db = connDao.getDb('Wiki')

        pwHash = hashlib.sha256(loginData['password'].encode())

        if regDao.checkUserId(db, loginData['userId']):
            userData = loginDao.getUserData(db, loginData['userId'])
            if userData['password'] == pwHash.hexdigest():
                token = loginDao.getLoginToken(db, loginData['userId'])
                return {
                    'result': 'success',
                    'token': token
                }
            else:
                return {'result': 'fail'}
        else:
            return {'result': 'fail'}


# 자동 로그인 처리
def autoLogin(tokenCookie):
    try:
        db = connDao.getDb('Wiki')
        userData = jwt.decode(tokenCookie, 'secret', algorithms=['HS256'])
        if loginDao.checkLoginToken(db, userData):
            return {
                'result': 'success',
                'userId': userData['userId']
            }
        else:
            return {'result': 'fail'}
    except jwt.exceptions.DecodeError:
        return {'result': 'fail'}


# 마이페이지 정보 확인
def getUserData(idData):
    db = connDao.getDb('Wiki')
    if regDao.checkUserId(db, idData['userId']):
        userData = {'result': 'success'}
        userData.update(mpDao.getUserDataForMyPage(db, idData['userId']))
        return userData
    else:
        return {'result': 'fail'}


# 유저 정보 수정
def updateUserData(userData):
    sampleData = {"userId": "", "password": "", "email": "", "name": "", "phoneNumber": ""}
    if userData.keys() != sampleData.keys():
        db = connDao.getDb('Wiki')

        pwHash = hashlib.sha256(userData['password'].encode())
        userData['password'] = pwHash.hexdigest()

        if regDao.checkUserId(db, userData['userId']) or not regDao.checkEmail(db, userData['email']):
            if userData['email'] == getUserData(userData)['email']:
                userId = userData['userId']
                del userData['userId']
                mpDao.updateUserInfo(db, userId, userData)
                return {'result': 'success'}
            return {'result': 'fail'}
        else:
            userId = userData['userId']
            del userData['userId']
            mpDao.updateUserInfo(db, userId, userData)
            return {'result': 'success'}
    else:
        return {'result': 'fail'}


# 회원 탈퇴
def deleteUser(userData):
    db = connDao.getDb('Wiki')
    if regDao.checkUserId(db, userData['userId']):
        userId = userData['userId']
        mpDao.deleteUser(db, userId)
        return {'result': 'success'}
    else:
        return {'result': 'fail'}
