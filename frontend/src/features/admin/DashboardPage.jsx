import { useEffect, useState } from 'react';
import API from '../../api/client';
import LoadingSpinner from '../../components/LoadingSpinner';

export default function DashboardPage() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    API.get('/dashboard/admin/')
      .then((res) => setStats(res.data))
      .catch(() => setStats(null))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;

  const cards = [
    ['Total Bookings', stats?.total_bookings ?? 0],
    ['Revenue', stats?.total_revenue ?? 0],
    ['Active Shows', stats?.active_shows ?? 0],
    ['Waitlist', stats?.waitlist_count ?? 0],
  ];

  return (
    <section className="shell-width px-6 py-10 md:py-14">
      <h1 className="marquee-title text-6xl md:text-7xl">Organiser</h1>
      <p className="mt-4 max-w-xl text-lg leading-snug text-[#9aa6c4]">
        A compact operational view for bookings, revenue, live shows and waitlist activity.
      </p>
      <div className="mt-8 grid gap-5 border-t border-[#273049] pt-8 md:grid-cols-2 xl:grid-cols-4">
        {cards.map(([label, value]) => (
          <div key={label} className="rounded-2xl border border-[#273049] bg-[#101525] p-6">
            <p className="text-xs font-black uppercase tracking-[0.18em] text-[#f4bd46]">{label}</p>
            <p className="mt-4 text-4xl font-black text-[#f8f4e8]">{value}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
