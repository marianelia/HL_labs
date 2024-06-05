from pydantic import BaseModel
from typing import List, Mapping
from datetime import datetime


class Tweet(BaseModel):
    user_id : str
    text: str
    create_date: datetime