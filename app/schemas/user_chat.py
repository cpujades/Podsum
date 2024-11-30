from pydantic import BaseModel


class UserChatMessageRequest(BaseModel):
    message: str
    podcast_id: str = None
    user_id: str = None


class UserChatMessageResponse(BaseModel):
    answer: str
    usage: int = None
