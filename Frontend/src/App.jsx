import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import UploadVoicePage from "./pages/UploadVoicePage";
import GenerateVoicePage from "./pages/GenerateVoicePage";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upload" element={<UploadVoicePage />} />
        <Route path="/generate" element={<GenerateVoicePage />} />
        <Route path="*" element={<HomePage />} />
      </Routes>
    </div>
  );
}

export default App;
