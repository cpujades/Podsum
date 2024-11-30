from fastapi import APIRouter, HTTPException
from app.schemas.user_chat import UserChatMessageRequest, UserChatMessageResponse
from app.services.embeddings_service import (
    create_user_embeddings,
    retrieve_important_passages,
)
from app.services.user_chat_service import respond_to_user_message


router = APIRouter()


@router.post("/user_chat", response_model=UserChatMessageResponse)
async def create_transcription(request: UserChatMessageRequest):
    try:
        query_embeddings = await create_user_embeddings(request.message)
        top_passages = await retrieve_important_passages(
            query_embeddings, request.podcast_id
        )
        response = await respond_to_user_message(request.message, top_passages)
        return UserChatMessageResponse(answer=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
