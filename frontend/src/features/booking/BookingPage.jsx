import { Link, useParams } from 'react-router-dom';

export default function BookingPage() {
  const { showId } = useParams();

  return (
    <section className="shell-width px-6 py-10 md:py-14">
      <h1 className="marquee-title text-6xl md:text-7xl">Reserve Seats</h1>
      <p className="mt-4 max-w-xl text-lg leading-snug text-[#9aa6c4]">
        Seat map integration is ready for the booking API. This page keeps the booking route active while seat selection is connected.
      </p>
      <div className="mt-8 rounded-2xl border border-[#273049] bg-[#101525] p-6">
        <p className="text-xs font-black uppercase tracking-[0.18em] text-[#f4bd46]">Selected show</p>
        <p className="mt-2 text-2xl font-black">{showId}</p>
        <Link to="/bookings" className="btn-gold mt-6 inline-block">View My Bookings</Link>
      </div>
    </section>
  );
}
