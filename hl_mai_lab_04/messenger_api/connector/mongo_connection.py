from motor.motor_asyncio import AsyncIOMotorClient


class MongoConnector:
    _instance = None

    @classmethod
    def get_collection(cls):
        if cls._instance is None:
            username = "root"
            password = "example"
            mongo_uri = f"mongodb://{username}:{password}@localhost:27017/"
            cls._instance = AsyncIOMotorClient(mongo_uri)
        database = cls._instance["arch"]
        collection = database["chats"]
        return collection
    
    @classmethod
    def get_collection_tweets(cls):
        if cls._instance is None:
            username = "root"
            password = "example"
            mongo_uri = f"mongodb://{username}:{password}@mongo:27017/"
            cls._instance = AsyncIOMotorClient(mongo_uri)
        database = cls._instance["arch"]
        collection = database["tweets"]
        return collection

