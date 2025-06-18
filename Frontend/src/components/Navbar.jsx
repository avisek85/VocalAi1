// src/components/Navbar.jsx
import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
  const location = useLocation();

  const linkStyle = (path) =>
    `px-4 py-2 rounded hover:bg-gray-200 ${
      location.pathname === path ? "bg-gray-300 font-semibold" : ""
    }`;

  return (
    <nav className="bg-white shadow p-4 flex gap-4">
      <Link to="/" className={linkStyle("/")}>
        Home
      </Link>
      <Link to="/upload" className={linkStyle("/upload")}>
        Upload Voice
      </Link>
      <Link to="/generate" className={linkStyle("/generate")}>
        Generate Speech
      </Link>
    </nav>
  );
}
