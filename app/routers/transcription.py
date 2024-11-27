from fastapi import APIRouter, HTTPException
from app.schemas.transcription import TranscriptionRequest, TranscriptionResponse
from app.services.transcription_service import transcribe_video

router = APIRouter()


@router.post("/transcription", response_model=TranscriptionResponse)
async def create_transcription(request: TranscriptionRequest):
    try:
        transcript = await transcribe_video(request.youtube_link)
        return TranscriptionResponse(transcript=transcript)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
