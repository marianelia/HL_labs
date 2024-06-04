from fastapi import APIRouter, HTTPException
from models.tweet_model import Tweet
from models.message_model import Message, ChatPtPModel
from chat_handler.social_network_handler import SocialNetworkHandler, ChatPtPHandler
router = APIRouter()

@router.post("/tweet")
async def add_tweet(data: Tweet):
    result = await SocialNetworkHandler.post_tweet(data)
    return {"tweet_id": result}


@router.get("/tweet/{user_id}")
async def get_tweets(user_id: str):
    tweets = await SocialNetworkHandler.get_tweets_by_user_id(user_id)
    if tweets:
        return tweets
    else:
        raise HTTPException(status_code=404, detail="Tweets not found")


@router.get("/chat/{chat_id}")
async def read_chat(chat_id: str):
    chat = await ChatPtPHandler.get_chat(chat_id)
    if chat:
        return chat
    else:
        raise HTTPException(status_code=404, detail="Chat not found")



@router.post("/chat/{chat_id}/message")
async def add_message(chat_id: str, message: Message):
    chat = await ChatPtPHandler.add_message(chat_id, message)
    if chat.modified_count == 1:
        return {"message": "Message added successfully"}
    else:
        raise HTTPException(status_code=404, detail="Chat not found")


@router.post("/chat/{chat_id}/member")
async def add_member(chat_id: str, member: int):
    chat = await ChatPtPHandler.add_member(chat_id, member)
    if chat.modified_count == 1:
        return {"message": "Member added successfully"}
    else:
        raise HTTPException(status_code=404, detail="Chat not found")


@router.post("/chat")
async def create_chat(chat: ChatPtPModel):
    chat_id = await ChatPtPHandler.add_chat(chat)
    return {"chat_id": chat_id}