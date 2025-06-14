# backend/api/tts.py

from fastapi import APIRouter, UploadFile, File, Form
import uuid
import shutil
from services.voice_generator import generate_voice

router = APIRouter()

@router.post("/generate-voice/")
async def generate_voice_api(
    file: UploadFile = File(...),
    text: str = Form(...)
):
    # Save the uploaded speaker sample
    speaker_path = f"Vuploads/{uuid.uuid4().hex}.wav"
    with open(speaker_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Define output audio path
    output_path = f"Voutputs/{uuid.uuid4().hex}_generated.wav"

    # Generate voice
    filename = generate_voice(text, speaker_path, output_path)

    return {"message": "Voice generated!", "file": filename}
