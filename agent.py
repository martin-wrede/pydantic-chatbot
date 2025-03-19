
from pydantic_ai import Agent
from pydantic import BaseModel, Field
import asyncio
import openai
from dotenv import load_dotenv
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()

# Define result model
class ChatResult(BaseModel):
    response: str = Field(description='Response from the chatbot')

# Create OpenAI chatbot agent
chat_agent = Agent(
    model='gpt-4',
    result_type=ChatResult,
    system_prompt='You are a helpful chatbot. Answer user queries in a friendly and informative way.',
)

# Function to interact with OpenAI API
async def chat_with_bot(user_input: str):
    result = await chat_agent.run(user_input)
    return result.data.response

# Create FastAPI app
app = FastAPI()

# Allow CORS for all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request and response models
class ChatRequest(BaseModel):
    user_input: str

class ChatResponse(BaseModel):
    response: str

# Define API endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    response = await chat_with_bot(request.user_input)
    return ChatResponse(response=response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)