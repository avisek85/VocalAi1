
export default function HomePage() {
  return (
    <div className="p-8 text-center space-y-4">
      <h1 className="text-3xl font-bold">Welcome to VocalAI</h1>
      <p className="text-gray-600">
        Create personalized voices and generate speech with ease.
      </p>
      <div className="flex justify-center gap-4 mt-6">
        <a
          href="/upload"
          className="bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600 transition"
        >
          Upload Voice
        </a>
        <a
          href="/generate"
          className="bg-green-500 text-white px-6 py-3 rounded hover:bg-green-600 transition"
        >
          Generate Speech
        </a>
      </div>
    </div>
  );
}