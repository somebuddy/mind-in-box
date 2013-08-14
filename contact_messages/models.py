from django.db import models


class Message(models.Model):
    sender_IP = models.IPAddressField(blank=True, default='127.0.0.1')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user_name = models.CharField(max_length=255, blank=True, default='')
    user_email = models.EmailField(blank=True, default='')
    content = models.TextField()
