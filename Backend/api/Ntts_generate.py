"""
api/voice_generate.py
----------------------
This module provides an API endpoint for generating speech from text.
Users can specify the voice by name and choose between 'coqui' or 'vakyansh' TTS models.

Dependencies to install:
- TTS (by coqui-ai)
- vakyansh-tts (unofficial Python wrapper or HTTP client)

Install Coqui TTS:
    pip install TTS

Note: Vakyansh integration will require additional setup, like REST API or CLI bridge.
"""


# api/voice_generate.py

from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import FileResponse
from db import Ndatabase
from pathlib import Path
import uuid
import os
import traceback
from models.TTSmodel import get_coqui_model
from models.Vakyanshmodel import run_vakyansh_tts

router = APIRouter()

# Create output directory
OUTPUT_DIR = Path("Voutputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/generate-voice")
def generate_voice(
    text: str = Form(...),
    voice_name: str = Form(...),
    model: str = Form("coqui")
):
    """
    Generate speech from text using a saved voice and selected model ('coqui' or 'vakyansh').
    """
    # Fetch voice sample path
    sample = Ndatabase.get_voice_sample(voice_name)
    if not sample:
        raise HTTPException(status_code=404, detail="Voice sample not found.")
    
    if not os.path.exists(sample.file_path):
        raise HTTPException(status_code=404, detail=f"Voice sample file missing: {sample.file_path}")

    output_path = OUTPUT_DIR / f"{uuid.uuid4()}.wav"

    # Coqui TTS
    if model == "coqui":
        try:
            print(f"[DEBUG] Generating voice using Coqui...")
            print(f"[DEBUG] Text: {text}")
            print(f"[DEBUG] Speaker WAV: {sample.file_path}")
            print(f"[DEBUG] Output Path: {output_path}")

            tts = get_coqui_model()  # load only once if your TTSmodel.py is optimized
            tts.tts_to_file(
                text=text,
                speaker_wav=sample.file_path,
                file_path=str(output_path),
                language="hi"
            )

        except Exception as e:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Coqui TTS error: {str(e)}")

    # Vakyansh TTS
    elif model == "vakyansh":
        try:
            output_path = run_vakyansh_tts(text=text, lang="hi", output_path=output_path)
        except Exception as e:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Vakyansh TTS error: {str(e)}")

    else:
        raise HTTPException(status_code=400, detail="Invalid model specified. Use 'coqui' or 'vakyansh'.")

    # Serve generated audio
    return FileResponse(
        path=output_path,
        filename=output_path.name,
        media_type='audio/wav'
    )




