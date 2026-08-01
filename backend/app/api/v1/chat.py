from fastapi import APIRouter

from app.models.ChatRequest import ChatRequest
from app.services import ai_service

router = APIRouter()

@router.post("/chat")
async def chat(chat_request: ChatRequest):
    return {"message": await ai_service.chat(chat_request.message)}
