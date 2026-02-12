import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from a secure .env file
load_dotenv()

app = FastAPI()

# Configure CORS to allow secure communication with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",                 # Local React development
        "https://your-frontend-name.vercel.app"  # Production frontend URL
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Groq client using a secured API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define the expected schema for incoming POST requests
class AffirmationRequest(BaseModel):
    name: str
    feeling: str

@app.post("/api/affirmation")
async def generate_affirmation(request: AffirmationRequest):
    # Server-side validation for non-empty inputs
    if not request.name.strip() or not request.feeling.strip():
        raise HTTPException(status_code=400, detail="Name and feeling are required.")

    try:
        # Direct integration with an LLM (Groq Llama-3.3-70b)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a supportive, empathetic assistant. Your goal is to provide "
                        "personalized affirmations. "
                        # Explicit safety guardrails against medical advice/crisis
                        "IMPORTANT: Do not provide medical, legal, or clinical advice. "
                        "Do not diagnose conditions. If the user mentions self-harm or a crisis, "
                        "respond with: 'I am so sorry you are feeling this way. Please reach out "
                        "to a professional or a crisis hotline immediately; you do not have to "
                        "go through this alone.' Otherwise, keep responses to 2-4 sentences, "
                        "warm, and address the user by name."
                    )
                },
                {"role": "user", "content": f"My name is {request.name} and I am feeling {request.feeling}."}
            ],
            model="llama-3.3-70b-versatile",
        )
        return {"affirmation": chat_completion.choices[0].message.content}
    
    except Exception as e:
        # Log error internally and return a user-friendly message
        print(f"Internal Error: {e}")
        raise HTTPException(status_code=502, detail="The AI architect is currently resting. Please try again soon!")