from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from apps.common.views import health_check, readiness_check

urlpatterns = [
    path('', include('django_prometheus.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.venues.urls')),
    path('api/v1/', include('apps.events.urls')),
    path('api/v1/', include('apps.bookings.urls')),
    path('api/v1/', include('apps.payments.urls')),
    path('api/v1/', include('apps.waitlist.urls')),
    path('api/v1/', include('apps.dashboard.urls')),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/health/', health_check, name='health-check'),
    path('api/v1/readiness/', readiness_check, name='readiness-check'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
