from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
import os

load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# pamięć rozmowy
messages = [
    {
        "role": "system",
        "content": "Jesteś pomocnym asystentem. Odpowiadaj krótko i jasno po polsku."
    }
]

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    messages.append({
        "role": "user",
        "content": req.message
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    bot_reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    return {
        "user_message": req.message,
        "bot_response": bot_reply
    }

@app.post("/reset")
def reset():
    global messages
    messages = [
        {
            "role": "system",
            "content": "Jesteś pomocnym asystentem. Odpowiadaj krótko i jasno po polsku."
        }
    ]
    return {"status": "conversation reset"}

# Frontend

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>AI Chatbot</title>
        <style>
    body {
        font-family: Arial, sans-serif;
        background: #2c2c2c;
        display: flex;
        justify-content: center;
        padding-top: 50px;
        color: white;
    }

    .chat {
        width: 500px;
        background: #3a3a3a;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }

    #messages {
        height: 300px;
        overflow-y: auto;
        border: 1px solid #555;
        padding: 10px;
        margin-bottom: 10px;
        background: #1e1e1e;
        color: white;
    }

    input {
        width: 75%;
        padding: 10px;
        background: #2b2b2b;
        color: white;
        border: 1px solid #555;
        border-radius: 5px;
    }

    button {
        padding: 10px;
        background: #4CAF50;
        border: none;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background: #45a049;
    }
    </style>
        </head>
        <body>
            <div class="chat">
                <h2>AI Chatbot</h2>
                <div id="messages"></div>
                <input id="userInput" placeholder="Napisz wiadomość...">
                <button onclick="sendMessage()">Wyślij</button>
            </div>
    
                <script>
            async function sendMessage() {
                const input = document.getElementById("userInput");
                const messages = document.getElementById("messages");
        
                const userMessage = input.value;
                if (!userMessage) return;
        
                messages.innerHTML += "<p><b>Ty:</b> " + userMessage + "</p>";
                input.value = "";
        
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        message: userMessage
                    })
                });
        
                const data = await response.json();
        
                messages.innerHTML += "<p><b>Bot:</b> " + data.bot_response + "</p>";
                messages.scrollTop = messages.scrollHeight;
        
                input.focus();
            }
        
            document.getElementById("userInput").addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                    event.preventDefault();
                    sendMessage();
                }
            });
        </script>
    </body>
    </html>
    """