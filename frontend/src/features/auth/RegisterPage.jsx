import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../../api/client";

export default function RegisterPage() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    password2: "",
    role: "CUSTOMER",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const submit = async (e) => {
    e.preventDefault();
    setError("");

    if (form.password !== form.password2) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      await API.post("/auth/register/", form);
      alert("Registration successful! Please login.");
      navigate("/login");
    } catch (err) {
      console.error(err);

      if (err.response?.data) {
        const messages = [];
        Object.entries(err.response.data).forEach(([key, value]) => {
          messages.push(`${key}: ${Array.isArray(value) ? value.join(", ") : value}`);
        });
        setError(messages.join("\n"));
      } else {
        setError("Registration failed.");
      }
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
        <Link to="/login" className="btn-dark">Login</Link>
      </header>

      <section className="mx-auto flex min-h-[calc(100vh-90px)] max-w-md items-center py-10">
        <form onSubmit={submit} className="w-full rounded-2xl border border-[#273049] bg-[#101525] p-8">
          <p className="mb-3 text-sm font-bold uppercase tracking-[0.24em] text-[#f4bd46]">Join SeatSprint</p>
          <h1 className="marquee-title mb-7 text-5xl">Create Account</h1>

          {error && <div className="mb-4 whitespace-pre-wrap rounded-xl border border-[#5f2841] bg-[#2a1322] p-3 text-sm font-semibold text-[#ff8dad]">{error}</div>}

          <div className="grid gap-4 sm:grid-cols-2">
            <input type="text" name="first_name" placeholder="First Name" value={form.first_name} onChange={handleChange} className="input-dark" required />
            <input type="text" name="last_name" placeholder="Last Name" value={form.last_name} onChange={handleChange} className="input-dark" required />
          </div>

          <div className="mt-4 space-y-4">
            <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} className="input-dark" required />
            <input type="password" name="password" placeholder="Password" value={form.password} onChange={handleChange} className="input-dark" required />
            <input type="password" name="password2" placeholder="Confirm Password" value={form.password2} onChange={handleChange} className="input-dark" required />
            <select name="role" value={form.role} onChange={handleChange} className="input-dark">
              <option value="CUSTOMER">Customer</option>
              <option value="ORGANISER">Organiser</option>
            </select>
          </div>

          <button type="submit" disabled={loading} className="btn-gold mt-6 w-full">
            {loading ? "Registering" : "Register"}
          </button>

          <p className="mt-6 text-center text-sm text-[#9aa6c4]">
            Already registered? <Link to="/login" className="font-bold text-[#f4bd46]">Login</Link>
          </p>
        </form>
      </section>
    </div>
  );
}
