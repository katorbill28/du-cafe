# frontend/models.py
from django.db import models

class Cafe(models.Model):
    CAMPUS_CHOICES = [
        ('north', 'North Campus'),
        ('south', 'South Campus'),
        ('off', 'Off Campus'),
    ]

    name = models.CharField(max_length=200)
    campus = models.CharField(max_length=10, choices=CAMPUS_CHOICES)
    short_intro = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    price_range = models.CharField(max_length=50, blank=True)   # e.g. "₹50-150"
    menu_text = models.TextField(blank=True)   # or use JSONField if structured
    image = models.ImageField(upload_to='cafes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_campus_display()})"
