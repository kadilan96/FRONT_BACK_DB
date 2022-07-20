from pymongo import MongoClient


# MongoDB 클라이언트 생성
def getClient(url='localhost', port=27017):
    client = MongoClient(url, port)
    print('MongoDB Connected')
    return client


# MongoDB 데이터베이스 생성
def getDb(dbName, client=getClient()):
    db = client[dbName]
    return db

