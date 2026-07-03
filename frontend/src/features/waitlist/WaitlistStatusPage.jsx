import { useEffect, useState } from 'react';
import API from '../../api/client';
import LoadingSpinner from '../../components/LoadingSpinner';

export default function WaitlistStatusPage() {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    API.get('/waitlist/')
      .then((res) => setEntries(res.data?.results || res.data || []))
      .catch(() => setEntries([]))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;

  return (
    <section className="shell-width px-6 py-10 md:py-14">
      <h1 className="marquee-title text-6xl md:text-7xl">Waitlist</h1>
      <p className="mt-4 max-w-xl text-lg leading-snug text-[#9aa6c4]">
        Track automatic offers for sold-out shows and held seats that return to inventory.
      </p>
      <div className="mt-8 border-t border-[#273049] pt-8">
        {entries.length ? (
          <div className="grid gap-4 md:grid-cols-2">
            {entries.map((entry) => (
              <div key={entry.id} className="rounded-2xl border border-[#273049] bg-[#101525] p-5">
                <p className="text-xs font-black uppercase tracking-[0.18em] text-[#f4bd46]">{entry.status}</p>
                <h2 className="mt-2 text-2xl font-black">Position {entry.position || '-'}</h2>
                <p className="mt-2 text-[#9aa6c4]">Requested seats: {entry.requested_seats || '-'}</p>
              </div>
            ))}
          </div>
        ) : (
          <div className="flex min-h-[280px] items-center justify-center text-center text-xl font-medium text-[#9aa6c4]">
            No waitlist entries yet.
          </div>
        )}
      </div>
    </section>
  );
}
