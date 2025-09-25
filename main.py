from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx
import json

# Load environment variables
load_dotenv()

# OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

OPENAI_API_BASE = "https://api.openai.com/v1"

app = FastAPI(title="OpenAI API Proxy")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 구체적인 origin을 지정하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTP 클라이언트 설정
async def get_openai_client():
    return httpx.AsyncClient(
        base_url=OPENAI_API_BASE,
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        },
        timeout=60.0,
    )

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    try:
        # 요청 본문 읽기
        body = await request.json()
        
        async with await get_openai_client() as client:
            response = await client.post("/chat/completions", json=body)
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/embeddings")
async def embeddings(request: Request):
    try:
        # 요청 본문 읽기
        body = await request.json()
        
        async with await get_openai_client() as client:
            response = await client.post("/embeddings", json=body)
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)