from django.db import models
from accounts.models import Profile


class MentorshipRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    mentor = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='received_requests',
        limit_choices_to={'role': 'mentor'}
    )
    seeker = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sent_requests',
        limit_choices_to={'role': 'seeker'}
    )

    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('mentor', 'seeker')
        ordering = ['-requested_at']

    def __str__(self):
        return f"{self.seeker.user.username} → {self.mentor.user.username}"


class MentorSession(models.Model):
    mentorship_request = models.ForeignKey(
        MentorshipRequest,
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    session_time = models.DateTimeField()
    topic = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} ({self.session_time})"
