from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def role_required(*allowed_roles):
    """
    Decorator to restrict access based on user role.
    Usage: @role_required('seeker', 'provider')
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapper(request, *args, **kwargs):
            if not hasattr(request.user, 'profile'):
                return redirect('register')
            
            user_role = request.user.profile.role
            if user_role not in allowed_roles:
                return redirect('unauthorized')
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def seeker_required(view_func):
    """Decorator to restrict access to job seekers only"""
    return role_required('seeker')(view_func)


def provider_required(view_func):
    """Decorator to restrict access to job providers only"""
    return role_required('provider')(view_func)


def mentor_required(view_func):
    """Decorator to restrict access to mentors only"""
    return role_required('mentor')(view_func)

