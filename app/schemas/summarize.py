from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    youtube_link: str
    user_id: str = None
    model: str = "gpt-4o-2024-11-20"


class SummarizeResponse(BaseModel):
    summary: str
    # usage: str


class SummarizeFormat(BaseModel):
    summary: str
