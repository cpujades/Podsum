from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    youtube_link: str
    user_id: str = None
    model: str = None


class SummarizeResponse(BaseModel):
    summary: str
    # usage: str


class SummarizeFormat(BaseModel):
    summary: str
