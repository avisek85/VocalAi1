from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
from pathlib import Path


encoder = VoiceEncoder()

def get_speaker_embedding(audio_path:str) -> list:
    """
    Extracts speaker embedding from an audio file.

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        list: Speaker embedding as a list of floats.
    """
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file {audio_path} does not exist.")
    
    wav = preprocess_wav(audio_path)
    embedding = encoder.embed_utterance(wav)
    
    return embedding.tolist()  # Convert numpy array to list   