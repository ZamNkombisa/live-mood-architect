🧘‍♂️ Live Mood Architect

A full-stack therapeutic affirmation generator. This app uses FastAPI on the backend and React (Vite) on the frontend, integrated with Groq (Llama 3) for empathetic, real-time responses.

🔗 Live Links
Live App (Frontend): []

API Endpoint (Backend): []

🛠 Features & Requirements Met
Full-Stack Integration: React frontend communicating with a FastAPI backend.

AI Safety Logic: Custom system prompting to prevent medical diagnoses and provide crisis resources (Self-harm intent detection).

Environment Hygiene: Secure handling of API keys via environment variables (Zero secrets committed to GitHub).

UX/UI: Responsive glassmorphism design with loading states and error handling.

⚙️ Local Setup

1. Backend
   Bash / Powershell
   cd backend
   python -m venv venv

# Activate: venv\Scripts\activate (Windows) or source venv/bin/activate (Mac)

pip install -r requirements.txt

# Create .env and add: GROQ_API_KEY

uvicorn main:app --reload

2. Frontend
   Bash / Powershell
   cd frontend
   npm install

# Create .env.local and add: VITE_API_URL=http://127.0.0.1:8000

npm run dev
🔐 Required Environment Variables
GROQ_API_KEY

VITE_API_URL: (Frontend) The URL of the deployed or local backend (Check top for deployed URL).

🚀 Deployment Steps
Backend: Deployed on Render as a Web Service. The GROQ_API_KEY was added via the Render "Environment" dashboard.

Frontend: Deployed on Vercel. CORS was configured in the backend to allow requests from the Vercel domain.

📈 Future Improvements
Unit Testing: Add pytest for the safety prompt to ensure 100% compliance with non-clinical boundaries.

Persistence: Implement a database (PostgreSQL/Supabase) to allow users to "heart" and save their favorite affirmations.

Rate Limiting: Implement backend throttling to prevent API abuse.
