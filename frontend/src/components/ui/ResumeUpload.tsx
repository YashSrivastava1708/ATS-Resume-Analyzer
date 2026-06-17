"use client";

import { useState } from "react";

export default function ResumeUpload() {
  const [fileName, setFileName] = useState("");

 /* return (
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
  );*/


  return (
  <div className="mt-12 flex flex-col items-center">

    <div className="w-full max-w-xl border-2 border-dashed rounded-2xl p-10 text-center">

      <h2 className="text-2xl font-semibold mb-4">
        📄 Resume Upload
      </h2>

      <p className="text-gray-600">
        Drag & Drop your resume here
      </p>

      <p className="my-4 text-gray-400">
        OR
      </p>

      <label
        htmlFor="resume"
        className="cursor-pointer inline-block px-6 py-3 bg-black text-white rounded-lg"
      >
        Choose Resume File
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

      <p className="mt-4 text-sm text-gray-500">
        Supported formats: PDF, DOC, DOCX
      </p>

      {fileName && (
        <p className="mt-4 text-green-600 font-medium">
          ✔ {fileName} selected
        </p>
      )}

    </div>

  </div>
);
}