from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import UserRegistrationForm, ProfileUpdateForm
from .decorators import seeker_required, provider_required, mentor_required


def home(request):
    """Home page - shows verified jobs"""
    from jobs.models import Job
    jobs = Job.objects.filter(is_verified=True).order_by('-created_at')[:10]
    return render(request, 'accounts/home.html', {'jobs': jobs})


def register(request):
    """User registration with role selection"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            # Profile is auto-created by signal, update it with role
            profile = user.profile
            profile.role = form.cleaned_data['role']
            profile.phone = form.cleaned_data.get('phone', '')
            profile.save()
            
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """User login with role-based redirection"""
    if request.user.is_authenticated:
        return redirect_to_dashboard(request.user)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect_to_dashboard(user)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html')


def redirect_to_dashboard(user):
    """Helper function to redirect based on user role"""
    if not hasattr(user, 'profile'):
        return redirect('register')
    
    role = user.profile.role
    if role == 'seeker':
        return redirect('seeker_dashboard')
    elif role == 'provider':
        return redirect('provider_dashboard')
    elif role == 'mentor':
        return redirect('mentor_dashboard')
    else:
        return redirect('home')


@login_required
def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile_view(request):
    """View and update user profile"""
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'accounts/profile.html', {'profile': profile, 'form': form})


def unauthorized(request):
    """Unauthorized access page"""
    return render(request, 'accounts/unauthorized.html')


# Role-based dashboard redirects
@seeker_required
def seeker_dashboard(request):
    """Job Seeker Dashboard"""
    from jobs.models import JobApplication
    profile = request.user.profile
    applications = JobApplication.objects.filter(seeker=profile).order_by('-applied_at')
    accepted_count = applications.filter(status='accepted').count()
    pending_count = applications.filter(status='pending').count()
    rejected_count = applications.filter(status='rejected').count()
    
    return render(request, 'accounts/seeker_dashboard.html', {
        'profile': profile,
        'applications': applications,
        'accepted_count': accepted_count,
        'pending_count': pending_count,
        'rejected_count': rejected_count,
    })


@provider_required
def provider_dashboard(request):
    """Job Provider Dashboard"""
    from jobs.models import Job, JobApplication
    profile = request.user.profile
    jobs = Job.objects.filter(provider=profile).order_by('-created_at')
    total_applications = JobApplication.objects.filter(job__provider=profile).count()
    pending_applications = JobApplication.objects.filter(job__provider=profile, status='pending').count()
    
    return render(request, 'accounts/provider_dashboard.html', {
        'profile': profile,
        'jobs': jobs,
        'total_applications': total_applications,
        'pending_applications': pending_applications,
    })


@mentor_required
def mentor_dashboard(request):
    """Mentor Dashboard"""
    from mentors.models import MentorshipRequest
    profile = request.user.profile
    requests = MentorshipRequest.objects.filter(mentor=profile).order_by('-requested_at')
    pending_count = requests.filter(status='pending').count()
    
    return render(request, 'accounts/mentor_dashboard.html', {
        'profile': profile,
        'requests': requests,
        'pending_count': pending_count,
    })


def chatbot_view(request):
    """Chatbot page"""
    return render(request, 'accounts/chatbot.html')


from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

@require_POST
def chatbot_api(request):
    """API endpoint for chatbot responses"""
    from .chatbot import HireHubChatbot
    
    try:
        data = json.loads(request.body)
        message = data.get('message', '').strip()
        
        if not message:
            return JsonResponse({'error': 'Message is required'}, status=400)
        
        chatbot = HireHubChatbot(user=request.user)
        response = chatbot.get_response(message)
        
        return JsonResponse({
            'success': True,
            'response': response
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
