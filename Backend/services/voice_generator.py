# backend/services/voice_generator.py
from models.TTSmodel import tts
from pathlib import Path

def generate_voice(text: str, speaker_wav_path: str, output_path: str):
    # Generate and save the TTS audio
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_wav_path,
        file_path=output_path,
    )
    return Path(output_path).name
