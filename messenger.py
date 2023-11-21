from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles


class Message(BaseModel):
    id: str
    content: str

messages = []

app = FastAPI()

@app.get("/message-get")
def read_message():
    return messages

@app.post("/message-send")
def create_message(message:Message):
    messages.append(message)
    return "메시지보내기 성공"




app.mount("/", StaticFiles(directory="frontend",html=True), name="frontend")



