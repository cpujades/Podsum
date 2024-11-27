from pydantic import BaseModel


class TranscriptionRequest(BaseModel):
    youtube_link: str
    user_id: str


class TranscriptionResponse(BaseModel):
    transcript: str
