# 🤖 AI Chatbot (FastAPI + OpenAI)

Simple AI chatbot built with FastAPI and OpenAI API.  
The application provides a REST API and a minimal web interface for real-time conversations.

---

## 🚀 Features

- 🤖 OpenAI API integration (LLM responses)
- ⚡ FastAPI backend
- 🔗 REST endpoint: `/chat`
- 🧠 Conversation memory (context-aware responses)
- 🌐 Simple frontend (HTML + JavaScript)
- 🌙 Dark mode UI
- 🔐 Environment variables support (`.env`)

---

## 🎬 Demo

<img width="626" height="533" alt="demo" src="https://github.com/user-attachments/assets/acd4a6e3-2b58-4681-adec-7ee95273b8c6" />

---

## 📡 API Example

### POST /chat

```json
{
  "message": "Hello, what is Python?"
}
```
Response

```json
{
  "user_message": "Hello, what is Python?",
  "bot_response": "Python is a high-level programming language..."
}
```

🛠️ Run Locally
pip install -r requirements.txt
uvicorn api:app --reload

Then open:

http://127.0.0.1:8000

📁 Project Structure
ai-chatbot-fastapi/
│
├── api.py          # FastAPI backend + frontend
├── main.py         # CLI chatbot version
├── .env.example    # environment variables example
├── requirements.txt
└── demo.gif

⚙️ Tech Stack
🐍 Python
⚡ FastAPI
🤖 OpenAI API
🌐 HTML + JavaScript

🔒 Notes

Create a .env file with your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

The .env file is ignored in .gitignore for security reasons.
