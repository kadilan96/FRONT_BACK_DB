def getUserDataForMyPage(db, userId):
    result = db['user'].find_one({"userId": userId})

    del result['_id']
    del result['password']
    del result['loginToken']

    return result


def updateUserInfo(db, userId, userData):
    db['user'].update_one(filter={"userId": userId}, update={'$set': userData})


def deleteUser(db, userId):
    db['user'].delete_one({"userId": userId})
