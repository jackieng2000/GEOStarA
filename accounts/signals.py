# accounts/signals.py
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    messages.success(request, 'You have successfully logged in!')