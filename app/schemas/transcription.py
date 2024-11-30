from pydantic import BaseModel


class TranscriptionRequest(BaseModel):
    youtube_link: str
    user_id: str = None


class TranscriptionResponse(BaseModel):
    transcript: str
