📄 VocalAI_Summary.md
markdown
Copy
Edit
# 🎤 VocalAI – Personalized Voice Cloning Web App

---

## 🧠 Project Overview

**VocalAI** is a production-grade, full-stack voice cloning application that enables users to upload short audio samples, name them for future use, and generate speech from text using the same voice. It supports two powerful TTS (Text-to-Speech) engines — **Coqui TTS** and **Vakyansh TTS** — offering multilingual, high-quality audio generation.

This project aims to deliver an intuitive and accurate voice synthesis platform without relying on paid APIs, while offering extensibility for real-world applications like accessibility tools, smart assistants, and media dubbing.

---

## 🏗️ Architecture Summary

| Layer      | Technology         |
|------------|--------------------|
| Frontend   | React.js + Tailwind |
| Backend    | FastAPI (Python)   |
| TTS Models | Coqui TTS, Vakyansh |
| Database   | SQLite (via SQLAlchemy) |
| Audio Libs | Librosa, Torchaudio |
| Storage    | Local File System  |
| Deployment | Local/Cloud Ready  |

---

## 🔁 End-to-End Flow

1. **User uploads a `.wav` voice sample** and assigns a custom name (e.g., "Salman").
2. The backend saves the file and metadata in a local folder and SQLite database.
3. User enters text and selects:
   - Previously saved voice
   - TTS model (`Coqui` or `Vakyansh`)
4. The backend synthesizes the speech using the selected model and returns the output `.wav` file.
5. The frontend provides playback and download options for the generated voice.

---

## 📦 Tools & Technologies Used

### ✅ Programming Language:
- **Python**: Main backend logic and ML integration.

### ✅ Frontend Stack:
- **React.js**: UI for user interaction.
- **Tailwind CSS**: Responsive styling.
- **Axios**: API requests to backend.

### ✅ Backend Stack:
- **FastAPI**: RESTful API server.
- **SQLAlchemy + SQLite**: Voice sample storage and querying.
- **Pydantic**: Request validation.
- **Uvicorn**: FastAPI ASGI server.

### ✅ Machine Learning:
- **Coqui TTS**: For custom speaker voice cloning and multi-lingual synthesis.
- **Vakyansh TTS**: High-quality Hindi TTS model via CLI or wrapper.
- **Resemblyzer (Optional)**: Can extract speaker embeddings (not used for full synthesis in current version).

### ✅ Audio Processing:
- **Librosa & Torchaudio**: Feature extraction and waveform manipulation.
- **Soundfile**: Audio read/write operations.
- **FFmpeg**: Audio format conversion (for Vakyansh, optional).

---

## 📁 Key Modules

### 📌 Backend Directory (Python)
backend/
├── main.py # FastAPI entrypoint
├── db.py # Voice database with SQLAlchemy
├── api/
│ ├── upload_voice.py # Upload endpoint
│ ├── list_voices.py # List saved voices
│ └── voice_generate.py # TTS synthesis route
├── models/
│ ├── TTSmodel.py # Coqui TTS wrapper
│ └── Vakyanshmodel.py # Vakyansh CLI/REST wrapper
└── Voutputs/ # Stores generated speech

shell
Copy
Edit

### 📌 Frontend Directory (React)
frontend/
├── src/
│ ├── pages/
│ │ ├── HomePage.jsx
│ │ ├── UploadVoicePage.jsx
│ │ └── GenerateVoicePage.jsx
│ ├── components/
│ │ └── Navbar.jsx
│ └── App.jsx
├── index.html
└── main.jsx

yaml
Copy
Edit

---

## 🔧 Installation Steps

### Backend (Python 3.10+)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
Key Python Requirements
nginx
Copy
Edit
fastapi
uvicorn
sqlalchemy
TTS
librosa
torchaudio
soundfile
For Vakyansh: follow setup for their TTS repo

Frontend (React + Vite)
bash
Copy
Edit
cd frontend
npm install
npm run dev
Then open: http://localhost:5173

🧪 API Overview
POST /api/upload-voice
Upload .wav file with voice_name.

GET /api/voices
Get all available voice names.

POST /api/generate-voice
Fields:

text: Input text

voice_name: Custom saved name

model: coqui or vakyansh

Returns: Generated .wav audio file.

💡 Advanced Features (Built-In or Ready to Add)
Feature	Status
🎛️ Multiple TTS models	✅ Supported
🗃️ Voice reference system	✅ Implemented
⏳ Loading spinner / UX handling	✅ Done
🎧 Audio preview/download	✅ Done
🧪 Evaluation Metrics	🔜 Planned
🧵 Background queue (Celery/RQ)	🔜 Optional
🔒 Auth + user separation	🔜 Optional
☁️ S3 / cloud audio storage	🔜 Optional

🌟 Innovation & Use Cases
💬 Language-specific Assistants: Hindi-English speech assistant via model toggle.

🔁 Multi-speaker cloning: Store multiple custom voices and switch at runtime.

♿ Accessibility tools: Generate audio content for users with speech impairments.

🎙️ Dubbing & Podcasts: Synthetic voice-over using sample voices.

🧠 Voice as Identity: Emotionally personalized AI bots or avatars.

📬 Contact
Author: Abhishek Singh

GitHub: @avisek85

Email: abhishek@example.com (replace with actual)

📜 License
This project is licensed under the MIT License — feel free to use and modify it!

yaml
Copy
Edit

---

Would you like this summary exported as a file (`VocalAI_Summary.md`) or pushed to your GitHub `README.md` too?
