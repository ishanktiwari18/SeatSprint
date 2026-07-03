import { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import API from '../../api/client';
import LoadingSpinner from '../../components/LoadingSpinner';

const demoEvents = [
  {
    id: 'demo-nightfall',
    title: 'Nightfall Protocol',
    event_type: 'MOVIE',
    venue_name: 'PVR Grand, Screen 3',
    start_time: '2026-07-12T19:30:00',
    accent: 'from-[#33254d] to-[#171d2d]',
  },
  {
    id: 'demo-solstice',
    title: 'Solstice Live — Arka',
    event_type: 'CONCERT',
    venue_name: 'Open Air Amphitheatre',
    start_time: '2026-07-20T18:00:00',
    accent: 'from-[#5b2436] to-[#171d2d]',
  },
  {
    id: 'demo-monsoon',
    title: 'The Long Monsoon',
    event_type: 'MOVIE',
    venue_name: 'INOX Metroplex',
    start_time: '2026-07-15T21:45:00',
    accent: 'from-[#233550] to-[#171d2d]',
  },
];

function formatDate(value) {
  if (!value) return 'Date announced soon';
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString('en-IN', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  });
}

function getVenueName(event) {
  return event.venue_name || event.venue?.name || event.venue || event.location || 'Venue to be announced';
}

function getType(event) {
  return String(event.event_type || event.type || 'MOVIE').toUpperCase();
}

function EventCard({ event }) {
  const type = getType(event);
  const isConcert = type.includes('CONCERT');
  const accent = event.accent || (isConcert ? 'from-[#5b2436] to-[#171d2d]' : 'from-[#33254d] to-[#171d2d]');
  const linkTarget = event.show_id ? `/shows/${event.show_id}` : event.id?.toString().startsWith('demo-') ? '/events' : `/events/${event.id}`;

  return (
    <Link to={linkTarget} className="block overflow-hidden rounded-2xl border border-[#273049] bg-[#131827]">
      <div className={`flex h-40 items-center justify-center bg-gradient-to-br ${accent}`}>
        <div className="rounded-xl border border-[#36405e] bg-[#101525]/70 px-5 py-4 text-center text-sm font-black uppercase tracking-[0.24em] text-[#f4bd46]">
          {isConcert ? 'Live' : 'Feature'}
        </div>
      </div>
      <div className="p-5">
        <p className="mb-2 text-xs font-black uppercase tracking-[0.18em] text-[#f4bd46]">{type}</p>
        <h2 className="text-2xl font-black tracking-[-0.03em] text-[#f8f4e8]">{event.title || event.name}</h2>
        <p className="mt-2 text-base font-medium text-[#9aa6c4]">{getVenueName(event)}</p>
        <p className="mt-2 text-sm font-medium text-[#9aa6c4]">{formatDate(event.start_time || event.date)}</p>
      </div>
    </Link>
  );
}

export default function EventListPage() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('ALL');

  useEffect(() => {
    let mounted = true;

    API.get('/public/events/')
      .then((res) => {
        if (!mounted) return;
        const payload = res.data?.results || res.data || [];
        setEvents(Array.isArray(payload) && payload.length ? payload : demoEvents);
      })
      .catch(() => {
        if (mounted) setEvents(demoEvents);
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });

    return () => {
      mounted = false;
    };
  }, []);

  const visibleEvents = useMemo(() => {
    if (filter === 'ALL') return events;
    return events.filter((event) => getType(event).includes(filter));
  }, [events, filter]);

  if (loading) return <LoadingSpinner />;

  return (
    <section className="shell-width px-6 py-10 md:py-14">
      <div className="grid gap-8 md:grid-cols-[1fr_auto] md:items-end">
        <div>
          <h1 className="marquee-title text-6xl text-[#f8f4e8] md:text-7xl">Now Booking</h1>
          <p className="mt-4 max-w-xl text-lg leading-snug text-[#9aa6c4]">
            Reserve your seats from a live venue map. Held seats release automatically if checkout is abandoned — sold-out shows offer an automatic waitlist.
          </p>
        </div>

        <div className="flex gap-3">
          {['ALL', 'MOVIE', 'CONCERT'].map((item) => (
            <button
              key={item}
              type="button"
              onClick={() => setFilter(item)}
              className={filter === item ? 'btn-gold px-5 py-3' : 'btn-dark px-5 py-3'}
            >
              {item === 'ALL' ? 'All' : item === 'MOVIE' ? 'Movies' : 'Concerts'}
            </button>
          ))}
        </div>
      </div>

      <div className="mt-8 border-t border-[#273049] pt-8">
        {visibleEvents.length ? (
          <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            {visibleEvents.map((event) => <EventCard key={event.id || event.title} event={event} />)}
          </div>
        ) : (
          <div className="flex min-h-[260px] items-center justify-center text-center text-lg font-medium text-[#9aa6c4]">
            No shows available yet.
          </div>
        )}
      </div>
    </section>
  );
}
