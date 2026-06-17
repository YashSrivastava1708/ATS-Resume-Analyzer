export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-5xl font-bold">
        ATS Resume Analyzer
      </h1>

      <p className="mt-4 text-lg">
        Analyze your resume and improve your ATS score.
      </p>

      <button className="mt-8 px-6 py-3 bg-black text-white rounded-lg">
        Upload Resume
      </button>
    </main>
  );
}