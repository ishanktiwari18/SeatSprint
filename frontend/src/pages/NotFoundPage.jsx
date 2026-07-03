import { Link } from 'react-router-dom';

export default function NotFoundPage() {
  return (
    <section className="shell-width px-6 py-16">
      <h1 className="marquee-title text-6xl md:text-7xl">Page Not Found</h1>
      <p className="mt-4 text-lg text-[#9aa6c4]">The page you requested does not exist.</p>
      <Link to="/events" className="btn-gold mt-8 inline-block">Back to Browse</Link>
    </section>
  );
}
