from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = (
        ('seeker', 'Job Seeker'),
        ('provider', 'Job Provider'),
        ('mentor', 'Mentor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='seeker')

    # Common
    phone = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)  # Admin only

    # Job Seeker fields
    skills = models.TextField(blank=True)
    experience = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    # Job Provider fields
    company_name = models.CharField(max_length=200, blank=True)
    company_description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    # Mentor fields
    expertise = models.TextField(blank=True)
    available_time = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

