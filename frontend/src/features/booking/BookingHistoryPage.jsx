import { useEffect, useState } from 'react';
import API from '../../api/client';
import LoadingSpinner from '../../components/LoadingSpinner';

export default function BookingHistoryPage() {
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    API.get('/bookings/')
      .then((res) => setBookings(res.data?.results || res.data || []))
      .catch(() => setBookings([]))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;

  return (
    <section className="shell-width px-6 py-10 md:py-14">
      <h1 className="marquee-title text-6xl md:text-7xl">My Bookings</h1>
      <p className="mt-4 max-w-xl text-lg leading-snug text-[#9aa6c4]">
        Cancel a booking to see the seat automatically re-offered to the next person on the waitlist.
      </p>
      <div className="mt-8 border-t border-[#273049] pt-8">
        {bookings.length ? (
          <div className="space-y-4">
            {bookings.map((booking) => (
              <div key={booking.id} className="rounded-2xl border border-[#273049] bg-[#101525] p-5">
                <p className="text-xs font-black uppercase tracking-[0.18em] text-[#f4bd46]">{booking.status || 'Booking'}</p>
                <h2 className="mt-2 text-2xl font-black">{booking.booking_number || `Booking ${booking.id}`}</h2>
                <p className="mt-2 text-[#9aa6c4]">Seats: {booking.total_seats || booking.items?.length || 'Reserved'}</p>
              </div>
            ))}
          </div>
        ) : (
          <div className="flex min-h-[280px] flex-col items-center justify-center text-center">
            <div className="mb-5 rounded-xl border border-[#4a2845] bg-[#231326] px-5 py-3 text-sm font-black uppercase tracking-[0.24em] text-[#ef3d7a]">Ticket</div>
            <p className="text-xl font-medium text-[#9aa6c4]">No bookings yet — reserve seats from Browse.</p>
          </div>
        )}
      </div>
    </section>
  );
}
