"""
VocalAI Backend - Entry Point
-----------------------------
This is the main application file for the VocalAI voice cloning backend.
It sets up the FastAPI app, initializes the database, and integrates API routes.

Project Features:
- Voice sample upload & registration
- Speaker reference-based speech synthesis (Coqui / Vakyansh)
- File retrieval & clean architecture

Modules:
- db.database: DB models, engine setup, and CRUD utilities
- api.voice_upload: Routes for uploading and accessing voice samples

Run:
    uvicorn main:app --reload
"""
from fastapi import FastAPI
from api import Nvoice_upload,Ntts_generate,voice_get_all
from db import Ndatabase
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI application
app = FastAPI(
    title="VocalAI: Personalized Voice Cloning API",
    description="Upload voice samples, generate speech using Coqui or Vakyansh models.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Crucial: allow all HTTP methods
    allow_headers=["*"],  # Crucial: allow custom headers like Content-Type
)
@app.get("/")
def read_root():
    return {"message":"VocalAI is running!"}

# Include all API routes from voice_upload.py
app.include_router(Nvoice_upload.router, prefix="/api", tags=["Voice Management"])
app.include_router(Ntts_generate.router, prefix="/api", tags=["TTS Generation"])
app.include_router(voice_get_all.router, prefix="/api", tags=["Voice Retrieval"])

# On startup, create all necessary DB tables
@app.on_event("startup")
def startup():
    Ndatabase.create_tables()