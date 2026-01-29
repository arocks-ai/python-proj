# Client send message only
from datetime import datetime
from pydantic import BaseModel, Field


# client send the message like {"message": "Hello World"}
class UserPostIn(BaseModel):
    message: str


# Server calculates these fields like id and created_at
class UserPost(UserPostIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
