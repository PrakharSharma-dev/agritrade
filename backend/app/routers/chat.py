
import asyncio
import json
import logging
import os
from typing import Literal

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from google import genai
from google.genai import types 


load_dotenv()

router = APIRouter(
    prefix="/api/chat",
    tags=["Chatbot"]
)

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    text: str = Field(min_length=1, max_length=4000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    language: Literal["en", "hi"] = "en"
    context: dict = Field(default_factory=dict)
    history: list[ChatMessage] = Field(default_factory=list)


SYSTEM_INSTRUCTION = """
You are AgriTrade Assistant, an agricultural information assistant.

Your purpose is to help farmers understand:
- Crop cultivation and general crop management.
- Agricultural storage and post-harvest handling.
- Mandi markets and agricultural price concepts.
- Selling, transportation and storage costs.
- AgriTrade price predictions and recommendations.

Rules:
1. Reply in Hindi when the requested language is Hindi.
   Otherwise reply in English.
2. Use simple, clear language suitable for farmers.
3. Use the supplied AgriTrade context when answering questions
   about the farmer's current inputs or recommendation.
4. Never invent live mandi prices, market data, predictions,
   profit figures or database information.
5. If required data is missing, clearly say so.
6. Explain that price forecasts are estimates, not guarantees.
7. Do not claim to execute transactions or book transport.
8. For serious crop disease or pesticide decisions, recommend
   consulting a qualified agricultural officer.
9. If a question is unrelated to agriculture or AgriTrade,
   politely guide the user back to those topics.
10. Be helpful, concise and respectful.
"""




def generate_gemini_reply(prompt: str) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("Gemini API key is not configured.")

    client = genai.Client(
        api_key=GEMINI_API_KEY,
        http_options=types.HttpOptions(
            timeout=60000
        )
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
            "temperature": 0.4,
            "max_output_tokens": 300,
        },
    )

    reply = response.text

    if not reply or not reply.strip():
        raise RuntimeError("Gemini returned an empty response.")

    return reply.strip()





@router.post("/")
async def chat_with_gemini(request: ChatRequest):
    if not GEMINI_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="Chatbot is not configured. Gemini API key is missing."
        )

    context_text = json.dumps(
        request.context,
        ensure_ascii=False,
        default=str
    )[:8000]

    conversation = []

    for item in request.history[-10:]:
        role = "Farmer" if item.role == "user" else "AgriTrade Assistant"
        conversation.append(f"{role}: {item.text}")

    history_text = "\n".join(conversation)

    language_name = "Hindi" if request.language == "hi" else "English"

    prompt = f"""
Respond in {language_name}.

AGRITrade FARMER CONTEXT:
{context_text}

PREVIOUS CONVERSATION:
{history_text if history_text else "No previous messages."}

CURRENT FARMER QUESTION:
{request.message}

Provide a helpful and clear answer.
Use actual context values where relevant.
Do not invent missing data.
"""

    try:
        reply = await asyncio.wait_for(
            asyncio.to_thread(generate_gemini_reply, prompt),
            timeout=65
        )

        return {
            "reply": reply,
            "message": reply,
            "model": GEMINI_MODEL
        }

    except asyncio.TimeoutError:
        logger.error("Gemini chatbot request timed out")

        raise HTTPException(
            status_code=504,
            detail="Gemini response timed out. Please try again."
        )

    except HTTPException:
        raise

    except Exception as e:
        logger.exception("Gemini chatbot request failed")

        raise HTTPException(
            status_code=502,
            detail=f"Gemini error: {str(e)}"
        )

    
    