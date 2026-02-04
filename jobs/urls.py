from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    
    # Job Seeker views
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('applications/<int:application_id>/', views.application_status, name='application_status'),
    
    # Job Reporting
    path('jobs/<int:job_id>/report/', views.report_job, name='report_job'),
    
    # Job Provider views
    path('provider/jobs/create/', views.create_job, name='create_job'),
    path('provider/jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('provider/jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('provider/jobs/<int:job_id>/applicants/', views.job_applicants, name='job_applicants'),
    path('provider/applications/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),
]

