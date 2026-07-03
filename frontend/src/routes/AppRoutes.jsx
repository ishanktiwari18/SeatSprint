import { Routes, Route, Navigate } from 'react-router-dom';
import AuthGuard from '../components/AuthGuard';
import MainLayout from '../layouts/MainLayout';
import LoginPage from '../features/auth/LoginPage';
import RegisterPage from '../features/auth/RegisterPage';
import EventListPage from '../features/events/EventListPage';
import ShowDetailPage from '../features/events/ShowDetailPage';
import BookingPage from '../features/booking/BookingPage';
import ConfirmPage from '../features/booking/ConfirmPage';
import BookingHistoryPage from '../features/booking/BookingHistoryPage';
import WaitlistStatusPage from '../features/waitlist/WaitlistStatusPage';
import DashboardPage from '../features/admin/DashboardPage';
import NotFoundPage from '../pages/NotFoundPage';

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route element={<MainLayout />}>
        <Route path="/events" element={<EventListPage />} />
        <Route path="/shows/:showId" element={<ShowDetailPage />} />
        <Route path="/booking/:showId" element={<AuthGuard><BookingPage /></AuthGuard>} />
        <Route path="/booking/:bookingId/confirm" element={<AuthGuard><ConfirmPage /></AuthGuard>} />
        <Route path="/bookings" element={<AuthGuard><BookingHistoryPage /></AuthGuard>} />
        <Route path="/waitlist" element={<AuthGuard><WaitlistStatusPage /></AuthGuard>} />
        <Route path="/dashboard" element={<AuthGuard><DashboardPage /></AuthGuard>} />
        <Route path="/" element={<Navigate to="/events" replace />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  );
}