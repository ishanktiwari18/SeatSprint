import { useEffect, useState } from 'react';
import API from '../../api/client';
import LoadingSpinner from '../../components/LoadingSpinner';

export default function VenueListPage() {
  const [venues, setVenues] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    API.get('/venues/')
      .then(res => setVenues(res.data.results || res.data))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;
  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Venues</h1>
      <ul>
        {venues.map(v => <li key={v.id} className="mb-2">{v.name} – {v.city}, capacity: {v.total_capacity}</li>)}
      </ul>
    </div>
  );
}