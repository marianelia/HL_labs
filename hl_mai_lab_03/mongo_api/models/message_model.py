from pydantic import BaseModel
from typing import List, Mapping
from datetime import datetime


class Message(BaseModel):
    message_text: str
    send_date: datetime
    member: int

class ChatPtPModel(BaseModel):
    first_user_id: int
    second_user_id: int
    messages: List[Mapping]

    
class ChatModel(BaseModel):
    #admins: List[int] #
    members: List[int]
   # chat_name: str #
    messages: List[Mapping]
    #is_PtP: bool #