// 1. Update UploadVoicePage.jsx with form and API call

// src/pages/UploadVoicePage.jsx
import { useState } from 'react';
import axios from 'axios';

function UploadVoicePage() {
  const [name, setName] = useState("");
  const [model, setModel] = useState("coqui");
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file || !name) {
      return setStatus("Please provide both name and a .wav file.");
    }

    try {
      const formData = new FormData();
      formData.append("voice_name", name);
      formData.append("model", model);
      formData.append("file", file);

      const response = await axios.post(
        "http://localhost:8000/api/upload-voice",
        formData
      );
      setStatus(`✅ Upload successful: ${response.data.message}`);
    } catch (err) {
      console.error(err);
      setStatus("❌ Upload failed. Check backend server.");
    }
  };

  return (
    <div className="p-8 max-w-xl mx-auto space-y-6">
      <h2 className="text-2xl font-bold text-center">Upload Your Voice</h2>
      <form
        onSubmit={handleSubmit}
        className="space-y-4 bg-white shadow p-6 rounded"
      >
        <div>
          <label className="block mb-1 font-medium">Voice Name</label>
          <input
            type="text"
            className="w-full border rounded p-2"
            placeholder="e.g., Abhishek"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>

        <div>
          <label className="block mb-1 font-medium">Select Model</label>
          <select
            value={model}
            onChange={(e) => setModel(e.target.value)}
            className="w-full border rounded p-2"
          >
            <option value="coqui">Coqui TTS</option>
            <option value="vakyansh">Vakyansh TTS</option>
          </select>
        </div>

        <div>
          <label className="block mb-1 font-medium">Upload WAV File</label>
          <input
            type="file"
            accept=".wav,.mp3,.flac"
            onChange={(e) => setFile(e.target.files[0])}
            className="w-full"
          />
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
        >
          Upload Voice
        </button>
      </form>

      {status && <p className="text-center mt-4 font-semibold">{status}</p>}
    </div>
  );
}

// ⚙️ Backend API Endpoint:
// POST http://localhost:8000/api/voice/upload
// Content-Type: multipart/form-data
// Body:
// - voice_name: string
// - file: .wav

// 2. (No changes needed in main.jsx or App.jsx here)
// ✅ Confirm backend is running at port 8000
// ✅ CORS should be enabled in backend (already handled)

// Next Step: Build Generate Voice Page Form with API Integration


export default UploadVoicePage