from django.db import transaction
from .models import Venue, Section, Row, Seat

class VenueService:
    @staticmethod
    @transaction.atomic
    def create_venue_with_layout(name, address, city, state, zip_code, sections_data):
        venue = Venue.objects.create(name=name, address=address, city=city, state=state, zip_code=zip_code)
        for section_info in sections_data:
            section = Section.objects.create(venue=venue, name=section_info['name'])
            for row_info in section_info.get('rows', []):
                row = Row.objects.create(section=section, row_label=row_info['row_label'])
                for seat_info in row_info.get('seats', []):
                    Seat.objects.create(row=row, seat_number=seat_info['seat_number'], seat_type=seat_info.get('seat_type','REGULAR'))
        venue.total_capacity = Seat.objects.filter(row__section__venue=venue).count()
        venue.save(update_fields=['total_capacity'])
        return venue
