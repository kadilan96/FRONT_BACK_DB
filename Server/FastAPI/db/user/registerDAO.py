import datetime
import hashlib


# 회원가입
def addUser(db, userInfoInput):
    pwHash = hashlib.sha256(userInfoInput['password'].encode())

    userInfo = {
        "userId": userInfoInput['userId'],
        "password": pwHash.hexdigest(),
        "email": userInfoInput['email'],
        "loginToken": datetime.datetime.utcnow() + datetime.timedelta(seconds=300),
        "name": "",
        "phoneNumber": "",
    }
    db['user'].insert_one(userInfo)


# UserId 중복 확인
def checkUserId(db, userId):
    if db['user'].find_one({'userId': userId}) is not None:
        return True
    else:
        return False


# Email 중복 확인
def checkEmail(db, email):
    if db['user'].find_one({'email': email}) is not None:
        return True
    else:
        return False
