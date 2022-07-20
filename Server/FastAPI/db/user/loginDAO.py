import jwt


# 로그인 시 토큰 생성
def getLoginToken(db, userId):
    userData = db['user'].find_one({'userId': userId})

    del userData['_id']
    userData.update({'loginToken': str(userData['loginToken'])})

    return jwt.encode(userData, 'secret', algorithm='HS256')


# 토큰 확인
def checkLoginToken(db, userData):
    dbData = db['user'].find_one({'userId': userData['userId']})

    if dbData is None:
        return False

    del dbData['_id']
    dbData.update({'loginToken': str(userData['loginToken'])})

    print(userData)
    print(dbData)

    if userData == dbData:
        return True
    else:
        return False


# 유저 데이터 조회
def getUserData(db, userId):
    return db['user'].find_one({'userId': userId})