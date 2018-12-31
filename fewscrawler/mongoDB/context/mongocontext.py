from pymongo import MongoClient


class MongoContext:

    def __init__(self):
        # initializing the MongoClient, this helps to
        # access the MongoDB databases and collections
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client['mydatabase']

