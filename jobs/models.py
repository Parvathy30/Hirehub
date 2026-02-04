from django.db import models
from django.utils import timezone
from accounts.models import Profile


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)
    employee_count = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # Admin verification

    created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'provider'}
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('IN', 'Internship'),
        ('CT', 'Contract'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'provider'},
        related_name='posted_jobs',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)
    skills_required = models.TextField(help_text="Comma-separated list of skills")
    experience_required = models.CharField(max_length=100, blank=True, help_text="e.g., '2-3 years', 'Fresher'")
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)  # Admin verification
    verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    def get_skills_list(self):
        """Return skills as a list"""
        return [skill.strip().lower() for skill in self.skills_required.split(',') if skill.strip()]

    def calculate_skill_match(self, seeker_profile):
        """Calculate skill match percentage with a job seeker"""
        if not seeker_profile.skills:
            return 0
        
        job_skills = set(self.get_skills_list())
        seeker_skills = set([s.strip().lower() for s in seeker_profile.skills.split(',') if s.strip()])
        
        if not job_skills:
            return 0
        
        matching_skills = job_skills.intersection(seeker_skills)
        match_percentage = (len(matching_skills) / len(job_skills)) * 100
        return round(match_percentage)

    def get_matching_skills(self, seeker_profile):
        """Get list of matching skills"""
        if not seeker_profile.skills:
            return []
        
        job_skills = set(self.get_skills_list())
        seeker_skills = set([s.strip().lower() for s in seeker_profile.skills.split(',') if s.strip()])
        return list(job_skills.intersection(seeker_skills))


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    seeker = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'seeker'},
        related_name='job_applications'
    )
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    skill_match_percentage = models.IntegerField(default=0)  # Stored skill match
    applied_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('job', 'seeker')  # Prevent duplicate applications
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.seeker} - {self.job}"

    def save(self, *args, **kwargs):
        # Calculate skill match on save
        if not self.skill_match_percentage:
            self.skill_match_percentage = self.job.calculate_skill_match(self.seeker)
        super().save(*args, **kwargs)


class JobReport(models.Model):
    """Model for reporting fake/fraudulent jobs"""
    REPORT_REASONS = [
        ('fake', 'Fake Job Posting'),
        ('scam', 'Potential Scam'),
        ('misleading', 'Misleading Information'),
        ('inappropriate', 'Inappropriate Content'),
        ('duplicate', 'Duplicate Posting'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('investigating', 'Under Investigation'),
        ('resolved', 'Resolved - Action Taken'),
        ('dismissed', 'Dismissed'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='reports')
    reported_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='job_reports'
    )
    reason = models.CharField(max_length=20, choices=REPORT_REASONS)
    description = models.TextField(help_text="Please provide details about your concern")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('job', 'reported_by')  # One report per user per job
        ordering = ['-created_at']

    def __str__(self):
        return f"Report: {self.job.title} - {self.get_reason_display()}"