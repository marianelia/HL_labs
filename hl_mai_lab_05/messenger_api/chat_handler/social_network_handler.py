from bson import ObjectId
from typing import Any
from connector.mongo_connection import MongoConnector
from models.message_model import Message, ChatPtPModel
from models.tweet_model import Tweet


'''Добавление записи на стену
- Загрузка стены пользователя
- Отправка сообщения пользователю
- Получение списка сообщения для пользователя
'''
class SocialNetworkHandler:
    _collection = None

    def __new__(cls):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection_tweets()
        return cls._instance
    
    @classmethod
    async def post_tweet(cls, data: Tweet):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection_tweets()
        insert_result = await cls._collection.insert_one(dict(data))
        inserted_id = str(insert_result.inserted_id)
        return inserted_id
    
    @classmethod
    async def get_tweets_by_user_id(cls, user_id: str):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection()
        db_tweets = []
        tweets = cls._collection.find({"user_id": user_id})
        async for tweet in tweets:
            db_tweets.append(cls.map_tweets(tweet))
        return db_tweets
    
    def map_tweets(cls, tweet: Any):
        if tweet is None:
            return None
        print(str(tweet['_id']))
        return Tweet(id=str(tweet['_id']), user_id=tweet['user_id'], 
                      text=tweet['text'], create_date=tweet['create_date'])



class ChatPtPHandler:
    _collection = None

    def __new__(cls):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection()
        return cls._instance

    @classmethod
    async def get_chat(cls, chat_id: str):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection()
        chat = await cls._collection.find_one({"_id": ObjectId(chat_id)})
        print(chat)
        if chat:
            chat["_id"] = str(chat["_id"])
        return chat

    @classmethod
    async def add_message(cls, chat_id: str, message: Message):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection()
        filter_query = {"_id": ObjectId(chat_id)}
        update_query = {"$push": {"messages": Message.model_dump(message)}}
        chat = await cls._collection.update_one(filter_query, update=update_query)
        return chat

    @classmethod
    async def add_member(cls, chat_id: str, member: int):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection()
        filter_query = {"_id": ObjectId(chat_id)}
        update_query = {"$push": {"members": member}}
        chat = await cls._collection.update_one(filter_query, update=update_query)
        return chat

    @classmethod
    async def add_chat(cls, chat: ChatPtPModel):
        if cls._collection is None:
            cls._collection = MongoConnector.get_collection()
        print(chat)
        print(ChatPtPModel.model_dump(chat))
        result = await cls._collection.insert_one(ChatPtPModel.model_dump(chat))
        inserted_id = str(result.inserted_id)
        return inserted_id
