from pymongo import MongoClient

class MongoStore:
    def __init__(self, db_name, collection_name):
        self.db_name = db_name
        self.collection_name = collection_name
        self._client = MongoClient('localhost', 27017)
        self._db = self._client[self.db_name]
        self._collection = self._db[self.collection_name]

    def insert_data(self, data):
        try:
            self._collection.insert_one(data)
        except Exception as e:
            raise e