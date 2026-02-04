from django.urls import path
from . import views

urlpatterns = [
    # Job Seeker views
    path('mentors/', views.mentor_list, name='mentor_list'),
    path('mentors/<int:mentor_id>/request/', views.request_mentorship, name='request_mentorship'),
    
    # Mentor views
    path('mentor/requests/', views.mentorship_requests, name='mentorship_requests'),
    path('mentor/requests/<int:request_id>/<str:action>/', views.respond_to_request, name='respond_to_request'),
    path('mentor/sessions/<int:mentorship_id>/create/', views.create_session, name='create_session'),
]

