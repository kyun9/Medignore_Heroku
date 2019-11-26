from __future__ import unicode_literals

from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    photo_file = models.ImageField(upload_to='medignore/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)