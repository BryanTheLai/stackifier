from stackifier import TraceHook, FileWriter, WhatsAppMetaAdapter, TwilioAdapter
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

trace = TraceHook(storage=FileWriter(path="logs/whatsapp_conversations.jsonl"))


@app.post("/webhook/meta")
async def meta_webhook(request: Request):
    payload = await request.json()
    
    adapter = WhatsAppMetaAdapter()
    event = adapter.to_event(payload)
    
    trace.on_event(event)
    trace.flush()
    
    return {"status": "success"}


@app.post("/webhook/twilio")
async def twilio_webhook(request: Request):
    payload = await request.form()
    payload_dict = dict(payload)
    
    adapter = TwilioAdapter()
    event = adapter.to_event(payload_dict)
    
    trace.on_event(event)
    trace.flush()
    
    return {"status": "success"}


@app.post("/api/agent/message")
async def handle_agent_response(request: Request):
    data = await request.json()
    phone_number = data.get("phone_number")
    user_message = data.get("message")
    
    trace.log_message(
        role="user",
        content=user_message,
        metadata={"phone_number": phone_number}
    )
    
    agent_response = "Your agent response here"
    
    trace.log_message(
        role="assistant",
        content=agent_response,
        metadata={"phone_number": phone_number}
    )
    
    trace.flush()
    
    return {"response": agent_response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
