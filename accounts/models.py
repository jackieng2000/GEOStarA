# account/models.py
from django.db import models
from django.contrib.auth.models import User

# Optional: Extend User model if needed
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=15)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userGroup = models.CharField(max_length=15, blank=True, help_text="User group (15 characters max)")
    activityDate = models.DateField(null=True, blank=True, help_text="Date of current activity")

    def __str__(self):
        return f"{self.user.username}'s profile"