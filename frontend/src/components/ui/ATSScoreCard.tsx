export default function ATSScoreCard() {
  return (
    <div className="mt-12 w-full max-w-xl border rounded-2xl p-8 shadow-sm">

      <h2 className="text-2xl font-bold text-center">
        ATS Score
      </h2>

      <p className="text-center text-5xl font-bold text-green-600 mt-4">
        85%
      </p>

      <div className="mt-8">
        <h3 className="font-semibold mb-3">
          Matched Skills
        </h3>

        <ul className="space-y-2">
          <li>✔ React</li>
          <li>✔ TypeScript</li>
          <li>✔ Next.js</li>
          <li>✔ Tailwind CSS</li>
        </ul>
      </div>

    </div>
  );
}