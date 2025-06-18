from transformers import VitsModel, VitsTokenizer
import soundfile as sf

tokenizer = VitsTokenizer.from_pretrained("ai4bharat/indic-tts-hi")
model = VitsModel.from_pretrained("ai4bharat/indic-tts-hi")

text = "नमस्ते! मैं आपकी क्या मदद कर सकता हूँ?"
inputs = tokenizer(text, return_tensors="pt")
waveform = model.generate_speech(inputs["input_ids"])[0]

sf.write("output.wav", waveform.numpy(), 22050)
