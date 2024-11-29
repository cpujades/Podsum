from fastapi import APIRouter, HTTPException
from app.schemas.summarize import SummarizeRequest, SummarizeResponse
from app.services.transcription_service import transcribe_video
from app.services.summarize_service import summarize_transcription

router = APIRouter()


@router.post("/summarize", response_model=SummarizeResponse)
async def create_transcription(request: SummarizeRequest):
    try:
        transcript = await transcribe_video(request.youtube_link)
        summary = await summarize_transcription(transcript)
        return SummarizeResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
