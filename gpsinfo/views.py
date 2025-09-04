# gpsinfo/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import GPSLocation, GPSLatest
from .serializers import GPSLocationSerializer, GPSLatestSerializer
from django.contrib.auth.models import User

class GPSLocationViewSet(viewsets.ModelViewSet):
    queryset = GPSLocation.objects.all()
    serializer_class = GPSLocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Save the GPSLocation
        gps_location = serializer.save(user=self.request.user)
        
        # Update or create GPSLatest
        GPSLatest.objects.update_or_create(
            user=self.request.user,
            defaults={
                'latitude': gps_location.latitude,
                'longitude': gps_location.longitude,
                'timestamp': gps_location.timestamp,
                'altitude': gps_location.altitude,
                'accuracy': gps_location.accuracy,
            }
        )

    @action(detail=False, methods=['get'], url_path='latest')
    def get_latest_locations(self, request):
        """
        Fetch the latest GPS location for all users.
        """
        user = request.user
        if user.is_authenticated:
            latest_locations = GPSLatest.objects.all()
            serializer = GPSLatestSerializer(latest_locations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)