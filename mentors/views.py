from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import MentorshipRequest, MentorSession
from .forms import MentorshipRequestForm, MentorSessionForm
from accounts.decorators import seeker_required, mentor_required
from accounts.models import Profile


@seeker_required
def request_mentorship(request, mentor_id):
    """Request mentorship from a mentor"""
    mentor = get_object_or_404(Profile, pk=mentor_id, role='mentor')
    seeker = request.user.profile
    
    # Check if already requested
    if MentorshipRequest.objects.filter(mentor=mentor, seeker=seeker).exists():
        messages.warning(request, 'You have already sent a mentorship request to this mentor.')
        return redirect('mentor_list')
    
    if request.method == 'POST':
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship_request = form.save(commit=False)
            mentorship_request.mentor = mentor
            mentorship_request.seeker = seeker
            mentorship_request.save()
            messages.success(request, 'Mentorship request sent successfully!')
            return redirect('seeker_dashboard')
    else:
        form = MentorshipRequestForm(initial={'mentor': mentor})
        form.fields['mentor'].widget = forms.HiddenInput()
    
    return render(request, 'mentors/request_mentorship.html', {
        'form': form,
        'mentor': mentor,
    })


@seeker_required
def mentor_list(request):
    """List all available mentors"""
    mentors = Profile.objects.filter(role='mentor', is_verified=True)
    return render(request, 'mentors/mentor_list.html', {'mentors': mentors})


@mentor_required
def mentorship_requests(request):
    """View all mentorship requests for a mentor"""
    mentor = request.user.profile
    requests = MentorshipRequest.objects.filter(mentor=mentor).order_by('-requested_at')
    
    return render(request, 'mentors/mentorship_requests.html', {
        'requests': requests,
    })


@mentor_required
def respond_to_request(request, request_id, action):
    """Accept or reject a mentorship request"""
    mentorship_request = get_object_or_404(MentorshipRequest, pk=request_id, mentor=request.user.profile)
    
    if action == 'accept':
        mentorship_request.status = 'accepted'
        mentorship_request.save()
        messages.success(request, 'Mentorship request accepted!')
    elif action == 'reject':
        mentorship_request.status = 'rejected'
        mentorship_request.save()
        messages.info(request, 'Mentorship request rejected.')
    
    return redirect('mentorship_requests')


@mentor_required
def create_session(request, mentorship_id):
    """Create a mentorship session"""
    mentorship = get_object_or_404(MentorshipRequest, pk=mentorship_id, mentor=request.user.profile, status='accepted')
    
    if request.method == 'POST':
        form = MentorSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.mentorship = mentorship
            session.save()
            messages.success(request, 'Session scheduled successfully!')
            return redirect('mentorship_requests')
    else:
        form = MentorSessionForm()
    
    return render(request, 'mentors/create_session.html', {
        'form': form,
        'mentorship': mentorship,
    })
