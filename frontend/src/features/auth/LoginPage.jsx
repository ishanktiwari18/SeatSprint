import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../../api/client";

export default function LoginPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const { data } = await API.post("/auth/login/", form);
      localStorage.setItem("access_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);
      navigate("/events");
    } catch {
      setError("Invalid email or password.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#070a12] px-5 text-[#f8f4e8]">
      <header className="flex h-[90px] items-center justify-between border-b border-[#273049]">
        <Link to="/events" className="flex items-end gap-4">
          <span className="marquee-brand text-3xl text-[#f4bd46]">SeatSprint</span>
          <span className="hidden pb-1 text-xs font-bold uppercase tracking-[0.3em] text-[#8e98b4] sm:inline">Movies & Concerts</span>
        </Link>
        <Link to="/register" className="btn-dark">Create account</Link>
      </header>

      <section className="mx-auto flex min-h-[calc(100vh-90px)] max-w-md items-center">
        <form onSubmit={submit} className="w-full rounded-2xl border border-[#273049] bg-[#101525] p-8">
          <p className="mb-3 text-sm font-bold uppercase tracking-[0.24em] text-[#f4bd46]">Welcome back</p>
          <h1 className="marquee-title mb-7 text-5xl">Login</h1>

          {error && <p className="mb-4 rounded-xl border border-[#5f2841] bg-[#2a1322] p-3 text-sm font-semibold text-[#ff8dad]">{error}</p>}

          <div className="space-y-4">
            <input
              className="input-dark"
              placeholder="Email"
              type="email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              required
            />
            <input
              className="input-dark"
              placeholder="Password"
              type="password"
              value={form.password}
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              required
            />
          </div>

          <button disabled={loading} className="btn-gold mt-6 w-full">
            {loading ? "Logging in" : "Login"}
          </button>

          <p className="mt-6 text-center text-sm text-[#9aa6c4]">
            New user? <Link className="font-bold text-[#f4bd46]" to="/register">Register</Link>
          </p>
        </form>
      </section>
    </div>
  );
}
