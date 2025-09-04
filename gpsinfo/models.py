# app/models.py
from django.db import models
from django.contrib.auth.models import User

class GPSLocation(models.Model):
    """
    Stores a user's GPS location at a specific moment in time.
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='gps_locations',
        help_text="The user associated with this GPS location.",
        null=True, blank=True,
    )
    latitude = models.FloatField(
        help_text="Latitude in decimal degrees (e.g., 37.7749)."
    )
    longitude = models.FloatField(
        help_text="Longitude in decimal degrees (e.g., -122.4194)."
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when the location was recorded."
    )
    altitude = models.FloatField(
        null=True,
        blank=True,
        help_text="Altitude in meters (optional, for future use)."
    )
    accuracy = models.FloatField(
        null=True,
        blank=True,
        help_text="GPS accuracy in meters (optional, from device)."
    )

    class Meta:
        indexes = [
            models.Index(fields=['user', 'timestamp']),
        ]
        ordering = ['-timestamp']
        verbose_name = 'GPS Location'
        verbose_name_plural = 'GPS Locations'

    def __str__(self):
        return f"{self.user.username} at ({self.latitude}, {self.longitude}) on {self.timestamp}"
# Create your models here.

class GPSLatest(models.Model):
    """
    Stores the most recent GPS location for each user.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='gps_latest',
        help_text="The user associated with this latest GPS location.",
        primary_key=True,
    )
    latitude = models.FloatField(
        help_text="Latitude in decimal degrees (e.g., 37.7749)."
    )
    longitude = models.FloatField(
        help_text="Longitude in decimal degrees (e.g., -122.4194)."
    )
    
    altitude = models.FloatField(
        null=True,
        blank=True,
        help_text="Altitude in meters (optional, for future use)."
    )
    accuracy = models.FloatField(
        null=True,
        blank=True,
        help_text="GPS accuracy in meters (optional, from device)."
    )
    timestamp = models.DateTimeField(
        help_text="Time when the location was recorded."
    )

    class Meta:
        verbose_name = 'Latest GPS Location'
        verbose_name_plural = 'Latest GPS Locations'

    def __str__(self):
        return f"{self.user.username}'s latest at ({self.latitude}, {self.longitude}) on {self.timestamp}"
