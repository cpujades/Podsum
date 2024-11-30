from pydantic import BaseModel


class EmbeddingsRequest(BaseModel):
    transcription: str
    podcast_id: str
    user_id: str


class EmbeddingsResponse(BaseModel):
    success: bool
