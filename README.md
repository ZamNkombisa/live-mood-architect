# 🏛️ Live Mood Architect

A full-stack AI-driven affirmation generator that provides personalized, empathetic responses based on the user's current headspace.

## 🔗 Live Links

- **Frontend (Vercel):** [https://live-mood-architect.vercel.app/]
- **Backend API (Render):** [https://live-mood-architect-backend.onrender.com]

## 🛠️ Tech Stack

- **Frontend:** React (Vite), Axios, CSS3 (Glassmorphism)
- **Backend:** FastAPI (Python), Pydantic
- **AI Model:** Llama-3-70b via Groq SDK
- **Deployment:** Vercel & Render

## 🛡️ Key Features & Requirements Met

- **AI Safety Guardrails:** Implemented a robust system prompt to prevent medical diagnoses and handle crisis-related keywords with professional resources.
- **Environment Hygiene:** Secured sensitive API keys using `python-dotenv` and hosting-level environment variables (no secrets committed to GitHub).
- **CORS Configuration:** Securely whitelisted production origins to allow cross-domain communication.
- **User Experience:** Implemented loading states and user-friendly error handling to manage API latency and potential downtime.

## 🚀 How to Run Locally

1. **Backend:**
   - `cd backend`
   - `pip install -r requirements.txt`
   - Create a `.env` with your `GROQ_API_KEY`
   - `uvicorn main:app --reload`

2. **Frontend:**
   - `cd frontend`
   - `npm install`
   - `npm run dev`
