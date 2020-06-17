__author__ = "DGOAT"

import pymongo

# definition of type of thing in real world
class Database(object):
    # static member variables in class
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

# this tag tells python we are not using self in this
#    method cuz it will belong to the class as a whole
 #   and not every instance gets their own
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["fullstack"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
