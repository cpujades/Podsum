from pydantic import BaseModel


class EmbeddingsRequest(BaseModel):
    transcription: str
    # podcast_id: str = None
    # user_id: str = None


class EmbeddingsResponse(BaseModel):
    success: bool
