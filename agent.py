from pydantic_ai import Agent
from pydantic import BaseModel, Field
import asyncio
import openai
from dotenv import load_dotenv
import os
import sys

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

# Run chatbot in CLI mode
async def main():
    print("Simple Chatbot (Type 'exit' to quit)")
    while True:
        if sys.stdin.isatty():
            user_input = input("You: ")
        else:
            user_input = "default input"  # Provide a default input or handle differently
        if user_input.lower() == "exit":
            break
        response = await chat_with_bot(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    asyncio.run(main())