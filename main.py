import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "Jesteś pomocnym asystentem. Odpowiadaj krótko i jasno po polsku."
    }
]

print("AI Chatbot")
print("Napisz 'exit', żeby zakończyć.\n")

while True:
    user_message = input("Ty: ")

    if user_message.lower() == "exit":
        print("Bot: Do zobaczenia!")
        break

    messages.append({
        "role": "user",
        "content": user_message
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

    print("Bot:", bot_reply)