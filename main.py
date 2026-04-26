from fastapi import FastAPI, Request
import requests
from ai import generate_response
from config import TELEGRAM_TOKEN

app = FastAPI()

@app.post(f"/webhook/telegram/{TELEGRAM_TOKEN}")
async def telegram(request: Request):
    data = await request.json()
    try:
        text = data["message"]["text"]
        chat_id = data["message"]["chat"]["id"]
        
        reply = generate_response(chat_id, text)
        
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": chat_id, "text": reply})
    except: pass
    return {"ok": True}

# Aquí agregaremos WhatsApp después
