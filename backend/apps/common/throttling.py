from rest_framework.throttling import UserRateThrottle

class BookingRateThrottle(UserRateThrottle):
    rate = '20/minute'
