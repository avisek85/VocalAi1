# models/Vakyanshmodel.py

import re
from vakyansh_tts.tts_infer.tts import TextToMel, MelToWav
from vakyansh_tts.tts_infer.transliterate import XlitEngine
from vakyansh_tts.tts_infer.num_to_word_on_sent import normalize_nums
from scipy.io.wavfile import write
import uuid
from pathlib import Path

# You can place these in a .env or config file
GLOW_MODEL_DIR = "C:\\Users\\DELL\\Downloads\\glow\\glow_ckp"
HIFI_MODEL_DIR = "C:\\Users\\DELL\\Downloads\\hifi\\hifi_ckp"
OUTPUT_DIR = Path("Voutputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def translit(text, lang):
    reg = re.compile(r'[a-zA-Z]')
    engine = XlitEngine(lang)
    words = [engine.translit_word(word, topk=1)[lang][0] if reg.match(word) else word for word in text.split()]
    return ' '.join(words)

def run_vakyansh_tts(text: str, lang: str = "hi", output_path: Path = None) -> Path:
    text = text.replace('।', '.')
    text = normalize_nums(text, lang)
    text = translit(text, lang)

    text_to_mel = TextToMel(glow_model_dir=GLOW_MODEL_DIR, device="cpu")
    mel_to_wav = MelToWav(hifi_model_dir=HIFI_MODEL_DIR, device="cpu")

    mel = text_to_mel.generate_mel(text)
    audio, sr = mel_to_wav.generate_wav(mel)

    if not output_path:
        output_path = OUTPUT_DIR / f"{uuid.uuid4()}.wav"

    write(output_path, sr, audio)
    return output_path
