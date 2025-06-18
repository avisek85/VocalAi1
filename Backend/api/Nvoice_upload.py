"""
api/voice_upload.py
--------------------
This module defines FastAPI routes for:
- Uploading `.wav` voice samples with a user-defined name
- Retrieving voice samples by name

Dependencies to install before running:
- fastapi
- uvicorn
- python-multipart (for form file upload)

Install via pip:
    pip install fastapi uvicorn python-multipart
"""

from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
import shutil
from db.Ndatabase import save_voice_sample, get_voice_sample

router = APIRouter()

# Directory to store uploaded voice samples
UPLOAD_DIR = Path("Vuploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload-voice")
def upload_voice(
    voice_name: str = Form(...),
    file: UploadFile = File(...)
):
    """
    Upload a voice sample (.wav file) and register it with a unique voice_name.
    """
    if not file.filename.endswith(('.wav', '.mp3', '.flac')):
        raise HTTPException(status_code=400, detail="Only ('.wav', '.mp3', '.flac') files are supported.")

    file_path = UPLOAD_DIR / f"{voice_name}.wav"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    save_voice_sample(voice_name=voice_name, file_path=str(file_path))

    return JSONResponse({
        "message": "Voice uploaded successfully.",
        "voice_name": voice_name
    })

@router.get("/get-voice/{voice_name}")
def get_voice(voice_name: str):
    """
    Retrieve a previously uploaded voice sample by name.
    """
    sample = get_voice_sample(voice_name)
    if not sample:
        raise HTTPException(status_code=404, detail="Voice sample not found.")

    file_path = Path(sample.file_path)
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File is missing from server.")

    return FileResponse(path=file_path, filename=file_path.name, media_type='audio/wav')
