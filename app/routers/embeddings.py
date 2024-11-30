from fastapi import APIRouter, HTTPException
from app.schemas.embeddings import EmbeddingsRequest, EmbeddingsResponse
from app.services.embeddings_service import (
    create_transcription_embeddings,
    insert_embeddings,
)

router = APIRouter()


@router.post("/embeddings", response_model=EmbeddingsResponse)
async def create_transcription(request: EmbeddingsRequest):
    try:
        embeddings_info = await create_transcription_embeddings(request.transcription)
        metadata = {
            "podcast_id": "test_podcast_id",
            "user_id": "test_user_id",
        }
        success = await insert_embeddings(embeddings_info, metadata)
        return EmbeddingsResponse(success=success)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
