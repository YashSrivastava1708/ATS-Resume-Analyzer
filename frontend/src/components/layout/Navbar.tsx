export default function Navbar() {
  return (
    <nav className="flex justify-between items-center px-8 py-4 border-b">
      <h1 className="text-xl font-bold">
        ATS Resume Analyzer
      </h1>

      <div className="flex gap-6">
        <a href="#">Home</a>
        <a href="#">Features</a>
        <a href="#">About</a>
      </div>
    </nav>
  );
}