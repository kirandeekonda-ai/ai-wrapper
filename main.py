import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(title="Gemini 2.0 Flash LLM Wrapper")

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class PromptRequest(BaseModel):
    prompt: str

class LLMResponse(BaseModel):
    response: str

@app.post("/generate", response_model=LLMResponse)
async def generate_content(request: PromptRequest):
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API key not set.")
    payload = {
        "contents": [{"parts": [{"text": request.prompt}]}]
    }
    params = {"key": GEMINI_API_KEY}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(GEMINI_API_URL, params=params, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            # Extract the response text from Gemini's response structure
            text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            if not text:
                raise HTTPException(status_code=502, detail="No response from LLM.")
            return {"response": text}
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Gemini API error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
