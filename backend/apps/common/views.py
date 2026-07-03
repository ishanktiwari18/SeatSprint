from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.core.cache import cache

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def readiness_check(request):
    try:
        connection.ensure_connection()
    except Exception:
        return Response({"status": "error", "detail": "Database unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    try:
        cache.get('readiness_test')
    except Exception:
        return Response({"status": "error", "detail": "Redis unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    return Response({"status": "ok"}, status=status.HTTP_200_OK)
