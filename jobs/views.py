from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import Job, JobApplication, Company, JobReport
from .forms import JobForm, JobApplicationForm, JobReportForm
from accounts.decorators import seeker_required, provider_required
from accounts.models import Profile


def job_list(request):
    """List all verified jobs with filtering and skill matching"""
    jobs = Job.objects.filter(is_verified=True, is_active=True).order_by('-created_at')
    
    # Filter by company
    company_id = request.GET.get('company')
    if company_id:
        jobs = jobs.filter(company_id=company_id)
    
    # Filter by job type
    job_type = request.GET.get('job_type')
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    
    # Filter by location
    location = request.GET.get('location')
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(skills_required__icontains=search_query) |
            Q(company__name__icontains=search_query)
        )
    
    # Calculate skill match for authenticated job seekers
    jobs_with_match = []
    user_profile = None
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        if request.user.profile.role == 'seeker':
            user_profile = request.user.profile
    
    for job in jobs:
        job_data = {
            'job': job,
            'skill_match': job.calculate_skill_match(user_profile) if user_profile else None,
            'matching_skills': job.get_matching_skills(user_profile) if user_profile else []
        }
        jobs_with_match.append(job_data)
    
    # Sort by skill match if user is a seeker
    if user_profile and request.GET.get('sort') == 'match':
        jobs_with_match.sort(key=lambda x: x['skill_match'] or 0, reverse=True)
    
    companies = Company.objects.all().order_by('name')
    locations = Job.objects.filter(is_verified=True).values_list('location', flat=True).distinct()
    
    return render(request, 'jobs/job_list.html', {
        'jobs_with_match': jobs_with_match,
        'companies': companies,
        'locations': locations,
        'selected_company': company_id,
        'selected_job_type': job_type,
        'selected_location': location,
        'search_query': search_query,
        'job_types': Job.JOB_TYPE_CHOICES,
        'user_profile': user_profile,
    })


def job_detail(request, job_id):
    """View job details with skill matching"""
    job = get_object_or_404(Job, pk=job_id, is_verified=True)
    
    # Check if user has already applied
    has_applied = False
    skill_match = None
    matching_skills = []
    has_reported = False
    
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        profile = request.user.profile
        if profile.role == 'seeker':
            has_applied = JobApplication.objects.filter(job=job, seeker=profile).exists()
            skill_match = job.calculate_skill_match(profile)
            matching_skills = job.get_matching_skills(profile)
        
        # Check if user has already reported this job
        has_reported = JobReport.objects.filter(job=job, reported_by=profile).exists()
    
    # Get report count for display
    report_count = job.reports.filter(status='pending').count()
    
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied,
        'skill_match': skill_match,
        'matching_skills': matching_skills,
        'has_reported': has_reported,
        'report_count': report_count,
    })


@seeker_required
def apply_job(request, job_id):
    """Apply for a job"""
    job = get_object_or_404(Job, pk=job_id, is_verified=True)
    profile = request.user.profile
    
    # Check if already applied
    if JobApplication.objects.filter(job=job, seeker=profile).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', job_id=job_id)
    
    # Calculate skill match
    skill_match = job.calculate_skill_match(profile)
    matching_skills = job.get_matching_skills(profile)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.seeker = profile
            application.skill_match_percentage = skill_match
            application.save()
            messages.success(request, f'Application submitted successfully! Your skill match: {skill_match}%')
            return redirect('seeker_dashboard')
    else:
        form = JobApplicationForm()
    
    return render(request, 'jobs/apply_job.html', {
        'form': form, 
        'job': job,
        'skill_match': skill_match,
        'matching_skills': matching_skills,
    })


@seeker_required
def application_status(request, application_id):
    """View application status"""
    application = get_object_or_404(JobApplication, pk=application_id, seeker=request.user.profile)
    return render(request, 'jobs/application_status.html', {'application': application})


@provider_required
def create_job(request):
    """Create a new job post"""
    profile = request.user.profile
    
    # Get companies created by this provider
    companies = Company.objects.filter(created_by=profile)
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        form.fields['company'].queryset = companies
        if form.is_valid():
            job = form.save(commit=False)
            job.provider = profile
            job.save()
            messages.success(request, 'Job posted successfully! It will be visible after admin verification.')
            return redirect('provider_dashboard')
    else:
        form = JobForm()
        form.fields['company'].queryset = companies
    
    return render(request, 'jobs/create_job.html', {'form': form})


@provider_required
def edit_job(request, job_id):
    """Edit a job post"""
    job = get_object_or_404(Job, pk=job_id, provider=request.user.profile)
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            # Reset verification if significant changes made
            job = form.save(commit=False)
            job.is_verified = False  # Require re-verification after edit
            job.verified_at = None
            job.save()
            messages.success(request, 'Job updated successfully! It will need re-verification.')
            return redirect('provider_dashboard')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})


@provider_required
def delete_job(request, job_id):
    """Delete a job post"""
    job = get_object_or_404(Job, pk=job_id, provider=request.user.profile)
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('provider_dashboard')
    
    return render(request, 'jobs/delete_job.html', {'job': job})


@provider_required
def job_applicants(request, job_id):
    """View applicants for a specific job with skill match sorting"""
    job = get_object_or_404(Job, pk=job_id, provider=request.user.profile)
    
    # Get filter parameters
    status_filter = request.GET.get('status')
    sort_by = request.GET.get('sort', '-applied_at')
    
    applications = JobApplication.objects.filter(job=job)
    
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Sorting
    if sort_by == 'skill_match':
        applications = applications.order_by('-skill_match_percentage')
    elif sort_by == '-skill_match':
        applications = applications.order_by('skill_match_percentage')
    else:
        applications = applications.order_by(sort_by)
    
    return render(request, 'jobs/job_applicants.html', {
        'job': job,
        'applications': applications,
        'status_filter': status_filter,
        'sort_by': sort_by,
    })


@provider_required
def update_application_status(request, application_id, status):
    """Update application status"""
    application = get_object_or_404(JobApplication, pk=application_id)
    
    # Verify the job belongs to the provider
    if application.job.provider != request.user.profile:
        messages.error(request, 'Unauthorized access.')
        return redirect('provider_dashboard')
    
    valid_statuses = ['pending', 'reviewed', 'shortlisted', 'rejected', 'hired']
    if status in valid_statuses:
        application.status = status
        if status != 'pending':
            application.reviewed_at = timezone.now()
        application.save()
        messages.success(request, f'Application status updated to {status}!')
    
    return redirect('job_applicants', job_id=application.job.id)


@login_required
def report_job(request, job_id):
    """Report a suspicious/fake job"""
    job = get_object_or_404(Job, pk=job_id)
    profile = request.user.profile
    
    # Check if already reported
    if JobReport.objects.filter(job=job, reported_by=profile).exists():
        messages.warning(request, 'You have already reported this job.')
        return redirect('job_detail', job_id=job_id)
    
    if request.method == 'POST':
        form = JobReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.job = job
            report.reported_by = profile
            report.save()
            messages.success(request, 'Thank you for reporting. Our team will review this job posting.')
            return redirect('job_detail', job_id=job_id)
    else:
        form = JobReportForm()
    
    return render(request, 'jobs/report_job.html', {'form': form, 'job': job})


def company_list(request):
    """List all companies"""
    companies = Company.objects.all().order_by('name')
    
    # Search
    search = request.GET.get('search')
    if search:
        companies = companies.filter(
            Q(name__icontains=search) |
            Q(industry__icontains=search) |
            Q(location__icontains=search)
        )
    
    return render(request, 'jobs/company_list.html', {
        'companies': companies,
        'search': search,
    })


def company_detail(request, company_id):
    """View company details and their jobs"""
    company = get_object_or_404(Company, pk=company_id)
    jobs = Job.objects.filter(company=company, is_verified=True, is_active=True).order_by('-created_at')
    
    return render(request, 'jobs/company_detail.html', {
        'company': company,
        'jobs': jobs,
    })
