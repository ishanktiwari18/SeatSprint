import threading
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.events.models import Event, Show, ShowSeat, Venue, Section, Row, Seat

@pytest.mark.django_db(transaction=True)
def test_concurrent_booking_same_seats():
    user1 = User.objects.create_user(email='u1@test.com', password='pass', role='CUSTOMER')
    user2 = User.objects.create_user(email='u2@test.com', password='pass', role='CUSTOMER')
    venue = Venue.objects.create(name="V", address="A", city="C", state="S")
    section = Section.objects.create(venue=venue, name="A")
    row = Row.objects.create(section=section, row_label="1")
    seat = Seat.objects.create(row=row, seat_number="1")
    event = Event.objects.create(title="E", organiser=user1)
    show = Show.objects.create(event=event, venue=venue, start_time="2026-07-02T10:00:00Z", end_time="2026-07-02T12:00:00Z")
    ShowSeat.objects.create(show=show, seat=seat, status='AVAILABLE')
    client1 = APIClient()
    client1.force_authenticate(user=user1)
    client2 = APIClient()
    client2.force_authenticate(user=user2)
    url = reverse('booking-initiate')
    data = {'show_id': str(show.id), 'seat_ids': [str(seat.id)]}
    results = []
    def book(client, data):
        response = client.post(url, data, format='json')
        results.append(response)
    t1 = threading.Thread(target=book, args=(client1, data))
    t2 = threading.Thread(target=book, args=(client2, data))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    success = sum(1 for r in results if r.status_code == 201)
    assert success == 1, "Exactly one booking should succeed"
    conflict = sum(1 for r in results if r.status_code == 409)
    assert conflict == 1, "The other should get 409 Conflict"
