import { useParams } from 'react-router-dom';

export default function ConfirmPage() {
  const { bookingId } = useParams();

  return (
    <section className="shell-width px-6 py-10 md:py-14">
      <h1 className="marquee-title text-6xl md:text-7xl">Confirm</h1>
      <p className="mt-4 max-w-xl text-lg leading-snug text-[#9aa6c4]">
        Complete checkout for the selected booking before the hold timer expires.
      </p>
      <div className="mt-8 rounded-2xl border border-[#273049] bg-[#101525] p-6">
        <p className="text-xs font-black uppercase tracking-[0.18em] text-[#f4bd46]">Booking ID</p>
        <p className="mt-2 text-2xl font-black">{bookingId}</p>
      </div>
    </section>
  );
}
