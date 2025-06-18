import { useEffect, useState } from "react";
import axios from "axios";

export default function GenerateVoicePage() {
  const [voices, setVoices] = useState([]);
  const [selectedVoice, setSelectedVoice] = useState("");
  const [model, setModel] = useState("coqui");
  const [text, setText] = useState("");
  const [audioUrl, setAudioUrl] = useState("");
  const [status, setStatus] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchVoices = async () => {
      try {
        const res = await axios.get("http://localhost:8000/api/voices");
        setVoices(res.data.voices);
      } catch (err) {
        console.error(err);
        setStatus("❌ Failed to load voices.");
      }
    };
    fetchVoices();
  }, []);

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!selectedVoice || !text) {
      setStatus("❌ Please select a voice and enter text.");
      return;
    }

    setIsLoading(true);
    setStatus("");
    setAudioUrl("");

    try {
      const formData = new FormData();
      formData.append("voice_name", selectedVoice);
      formData.append("model", model);
      formData.append("text", text);

      const response = await axios.post(
        "http://localhost:8000/api/generate-voice",
        formData,
        { responseType: "blob" }
      );

      const blob = new Blob([response.data], { type: "audio/wav" });
      const url = URL.createObjectURL(blob);
      setAudioUrl(url);
      setStatus("✅ Voice generated successfully.");
    } catch (error) {
      console.error(error);
      setStatus("❌ Error generating voice.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-8 max-w-xl mx-auto space-y-6">
      <h2 className="text-3xl font-bold text-center">Generate Speech</h2>

      <form
        onSubmit={handleGenerate}
        className="space-y-4 bg-white p-6 shadow rounded"
      >
        <div>
          <label className="block mb-1 font-medium">Select Voice</label>
          <select
            value={selectedVoice}
            onChange={(e) => setSelectedVoice(e.target.value)}
            className="w-full p-2 border rounded"
          >
            <option value="">-- Select --</option>
            {voices.map((v) => (
              <option key={v} value={v}>
                {v}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="block mb-1 font-medium">Select Model</label>
          <select
            value={model}
            onChange={(e) => setModel(e.target.value)}
            className="w-full p-2 border rounded"
          >
            <option value="coqui">Coqui</option>
            <option value="vakyansh">Vakyansh</option>
          </select>
        </div>

        <div>
          <label className="block mb-1 font-medium">Text to Synthesize</label>
          <textarea
            rows="4"
            className="w-full p-2 border rounded"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type something..."
          ></textarea>
        </div>

        <button
  type="submit"
  disabled={isLoading}
  className="w-full bg-green-600 text-white p-2 rounded hover:bg-green-700 disabled:opacity-50"
>
  {isLoading ? (
    <span className="flex justify-center items-center gap-2">
      <span className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
      Generating...
    </span>
  ) : (
    "Generate"
  )}
</button>

      </form>

      {isLoading && (
        <div className="flex flex-col items-center mt-6 animate-pulse text-gray-700">
          <span className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>

          <p>Generating your voice... hang tight! 🎤✨</p>
        </div>
      )}

      {status && (
        <p className="text-center mt-4 font-semibold transition-all duration-300">
          {status}
        </p>
      )}

      {audioUrl && (
        <div className="text-center mt-6">
          <audio controls src={audioUrl} className="mx-auto" />
          <div className="mt-2">
            <a
              href={audioUrl}
              download
              className="text-blue-600 underline hover:text-blue-800"
            >
              ⬇️ Download Audio
            </a>
          </div>
        </div>
      )}
    </div>
  );
}
