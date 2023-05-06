from django.db import models


class Dream(models.Model):
    dream = models.TextField()
    dream_date = models.DateField()
    sleep_time = models.TimeField()
    wake_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

