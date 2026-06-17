export default function ResumeUpload() {
  return (
    <div className="mt-12 flex flex-col items-center">

      <label
        htmlFor="resume"
        className="cursor-pointer px-6 py-3 bg-black text-white rounded-lg"
      >
        Choose Resume
      </label>

      <input
        id="resume"
        type="file"
        accept=".pdf,.doc,.docx"
        className="hidden"
      />

      <p className="mt-3 text-sm text-gray-500">
        Supported formats: PDF, DOC, DOCX
      </p>

    </div>
  );
}