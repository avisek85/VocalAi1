from fastapi import FastAPI
from api import speaker,tts

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"VocalAI is running!"}

app.include_router(speaker.router) 
app.include_router(tts.router)