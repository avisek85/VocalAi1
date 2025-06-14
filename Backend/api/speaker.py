from fastapi import APIRouter , UploadFile, File
import shutil
import uuid
from services.speaker_encoder import get_speaker_embedding

router = APIRouter()

@router.post("/upload-audio/")
async def upload_audio(file:UploadFile = File(...)):
    """
    Uploads an audio file and returns its speaker embedding.
    
    Args:
        file (UploadFile): The audio file to be uploaded.
        
    Returns:
        dict: A dictionary containing the speaker embedding.
    """
    if not file.filename.endswith(('.wav', '.mp3', '.flac')):
        return {"error": "Invalid file format. Please upload a .wav, .mp3, or .flac file."}
    
    # Save the uploaded file to a temporary location
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # Get the speaker embedding
    embedding = get_speaker_embedding(temp_filename)
    
    # # Clean up the temporary file
    # os.remove(temp_file_path)
    
    return {"embedding": embedding}