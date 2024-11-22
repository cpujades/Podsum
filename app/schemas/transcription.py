from pydantic import BaseModel


class Transcription(BaseModel):
    yotube_link: str
