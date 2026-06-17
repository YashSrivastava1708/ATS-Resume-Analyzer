//using the navbar thus created
/*
import Navbar from "../components/layout/Navbar";
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
}*/
import ATSScoreCard from "../components/ui/ATSScoreCard";
import ResumeUpload from "../components/ui/ResumeUpload";

import Navbar from "../components/layout/Navbar";

export default function Home() {
  return (
    <>
      <Navbar />

      <main className="min-h-screen flex flex-col items-center justify-center px-4">

  <p className="text-blue-600 font-semibold mb-4">
    AI Powered Resume Screening
  </p>

  <h1 className="text-6xl font-bold text-center max-w-4xl">
    Get Your ATS Score Before Recruiters Do
  </h1>

  <p className="mt-6 text-xl text-center text-gray-600 max-w-2xl">
    Upload your resume, compare it against job descriptions,
    identify missing skills, and improve your chances of
    getting shortlisted.
  </p>

  {/* <div className="flex gap-4 mt-10">
    <button className="px-6 py-3 bg-black text-white rounded-lg">
      Upload Resume
    </button> */}
    
    {/* <button className="px-6 py-3 border rounded-lg">
      Learn More
    </button>
  </div> */}
  <ResumeUpload />
      {/* <ATSScoreCard/> */}
      <ATSScoreCard score={95} />

</main>
    </>
  );
}