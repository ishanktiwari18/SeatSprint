import { NavLink, Outlet } from 'react-router-dom';

function NavPill({ to, children }) {
  return (
    <NavLink
      to={to}
      className={({ isActive }) =>
        [
          'rounded-lg px-5 py-3 text-sm font-extrabold transition-none',
          isActive
            ? 'bg-[#f4bd46] text-[#11131b] ring-2 ring-[#f8df9e] ring-offset-2 ring-offset-[#101525]'
            : 'text-[#9aa6c4]'
        ].join(' ')
      }
    >
      {children}
    </NavLink>
  );
}

export default function MainLayout() {
  return (
    <div className="min-h-screen bg-[#070a12] text-[#f8f4e8]">
      <header className="border-b border-[#273049] bg-[#090d16]">
        <div className="flex h-[90px] items-center justify-between px-7">
          <NavLink to="/events" className="flex items-end gap-4">
            <span className="marquee-brand text-3xl text-[#f4bd46]">SeatSprint</span>
            <span className="hidden pb-1 text-xs font-bold uppercase tracking-[0.3em] text-[#8e98b4] sm:inline">
              Movies & Concerts
            </span>
          </NavLink>

          <nav className="absolute left-1/2 hidden -translate-x-1/2 rounded-xl border border-[#273049] bg-[#101525] p-1 md:flex">
            <NavPill to="/events">Browse</NavPill>
            <NavPill to="/bookings">My Bookings</NavPill>
            <NavPill to="/dashboard">Organiser</NavPill>
          </nav>

          <div className="flex items-center gap-3 text-sm text-[#9aa6c4]">
            <span className="hidden sm:inline">Demo TTL</span>
            <select className="rounded-lg border border-[#273049] bg-[#1a2135] px-4 py-3 font-bold text-[#f8f4e8] outline-none">
              <option>60s hold</option>
              <option>90s hold</option>
            </select>
          </div>
        </div>

        <nav className="flex gap-2 border-t border-[#273049] px-5 py-3 md:hidden">
          <NavPill to="/events">Browse</NavPill>
          <NavPill to="/bookings">My Bookings</NavPill>
          <NavPill to="/dashboard">Organiser</NavPill>
        </nav>
      </header>

      <main>
        <Outlet />
      </main>
    </div>
  );
}
