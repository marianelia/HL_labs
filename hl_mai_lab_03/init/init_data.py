from faker import Faker
from pymongo import MongoClient
import random
from bson import ObjectId
from datetime import datetime, timedelta


class MongoConnector:
    _instance = None

    @classmethod
    def get_collection(cls):
        if cls._instance is None:
            username = "root"
            password = "example"
            mongo_uri = f"mongodb://{username}:{password}@mongo:27017/"
            cls._instance = MongoClient(mongo_uri)
        database = cls._instance["arch"]
        collection = database["ptp"]
        return collection
    
    @classmethod
    def get_collection_tweets(cls):
        if cls._instance is None:
            username = "root"
            password = "example"
            mongo_uri = f"mongodb://{username}:{password}@mongo:27017/"
            cls._instance = MongoClient(mongo_uri)
        database = cls._instance["arch"]
        collection = database["tweets"]
        return collection


chats_collection = MongoConnector.get_collection()

tweets_collection = MongoConnector.get_collection_tweets()


class Initializer():

    @staticmethod
    def random_date(start_date, end_date):
        time_between_dates = end_date - start_date
        random_number_of_days = random.randrange(time_between_dates.days)
        random_date = start_date + timedelta(days=random_number_of_days)
        return random_date
    
    @staticmethod
    def generate_tweet():
        fake = Faker()
        tweet = {}
        tweet["user_id"] = str(ObjectId())
        tweet["text"] = fake.text()
        tweet['create_date'] = Initializer.random_date(
            datetime(2022, 1, 1), datetime.now())
        return tweet
    
    def generate_tweets(num):
        return [Initializer.generate_tweet() for _ in range(num)]
    

    @staticmethod
    def generate_chat():
        fake = Faker()
        chat = {}
        chat['is_PtP'] = random.choice([True, False])
        members = []
        members.append(fake.unique.pyint(min_value=0, max_value=9999))
        members.append(fake.unique.pyint(min_value=0, max_value=9999))
        chat['members'] = members
        chat['messages'] = []
        for _ in range(random.randint(10, 100)):
            message = {}
            message['message_text'] = fake.text()
            message['send_date'] = Initializer.random_date(
                datetime(2022, 1, 1), datetime.now())
            message['member'] = random.choice(chat['members'])
            chat['messages'].append(message)
        return chat
    
    def generate_chats(num):
        return [Initializer.generate_chat() for _ in range(num)]

if not chats_collection.find_one():
    num_chats = 100
    chats = Initializer.generate_chats(num_chats)
    chats_collection.insert_many(chats)
print(chats_collection.find_one())


if not tweets_collection.find_one():
    num_tweets = 100
    tweets = Initializer.generate_tweets(num_tweets)
    tweets_collection.insert_many(tweets)
print(tweets_collection.find_one())