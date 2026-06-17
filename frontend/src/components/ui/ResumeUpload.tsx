"use client";

import { useState } from "react";

export default function ResumeUpload() {
  const [fileName, setFileName] = useState("");

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
        onChange={(e) => {
          const file = e.target.files?.[0];

          if (file) {
            setFileName(file.name);
          }
        }}
      />

      <p className="mt-3 text-sm text-gray-500">
        Supported formats: PDF, DOC, DOCX
      </p>

      {fileName && (
        <p className="mt-4 text-green-600 font-medium">
          ✔ {fileName} selected
        </p>
      )}

    </div>
  );
}