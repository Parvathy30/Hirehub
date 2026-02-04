# HireHub Project Structure

## Complete Folder Structure

```
HireHub/
│
├── accounts/                          # User Authentication & Profiles App
│   ├── __init__.py
│   ├── admin.py                       # Admin configuration for Profile
│   ├── apps.py                        # App configuration with signals
│   ├── decorators.py                  # Role-based access decorators
│   ├── forms.py                       # Registration & profile forms
│   ├── models.py                      # Profile model
│   ├── signals.py                     # Auto-create profile signals
│   ├── urls.py                        # URL routing
│   ├── views.py                       # Authentication & dashboard views
│   ├── tests.py
│   │
│   ├── migrations/                    # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── ... (other migrations)
│   │
│   ├── static/                        # Static files
│   │   └── admin/
│   │       └── js/
│   │           └── profile_admin.js
│   │
│   └── templates/accounts/            # Account templates
│       ├── home.html                  # Home page
│       ├── register.html              # Registration page
│       ├── login.html                  # Login page
│       ├── profile.html                # Profile management
│       ├── seeker_dashboard.html       # Job seeker dashboard
│       ├── provider_dashboard.html     # Job provider dashboard
│       ├── mentor_dashboard.html       # Mentor dashboard
│       └── unauthorized.html           # Unauthorized access page
│
├── jobs/                              # Jobs & Companies App
│   ├── __init__.py
│   ├── admin.py                       # Admin for Company, Job, JobApplication
│   ├── apps.py                        # App configuration
│   ├── forms.py                       # Job & application forms
│   ├── models.py                      # Company, Job, JobApplication models
│   ├── urls.py                        # URL routing
│   ├── views.py                       # Job CRUD & application views
│   ├── tests.py
│   │
│   ├── migrations/                    # Database migrations
│   │   └── __init__.py
│   │
│   ├── management/                    # Management commands
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── populate_companies.py  # Command to populate 100+ companies
│   │
│   └── templates/jobs/                # Job templates
│       ├── job_list.html              # Job listing page
│       ├── job_detail.html            # Job details page
│       ├── apply_job.html             # Apply for job
│       ├── application_status.html    # View application status
│       ├── create_job.html            # Create job (provider)
│       ├── edit_job.html              # Edit job (provider)
│       ├── delete_job.html            # Delete job (provider)
│       ├── job_applicants.html        # View applicants (provider)
│       ├── company_list.html          # Company listing
│       └── company_detail.html        # Company details
│
├── mentors/                            # Mentorship App
│   ├── __init__.py
│   ├── admin.py                       # Admin for MentorshipRequest, MentorSession
│   ├── apps.py                        # App configuration
│   ├── forms.py                       # Mentorship forms
│   ├── models.py                      # MentorshipRequest, MentorSession models
│   ├── urls.py                        # URL routing
│   ├── views.py                       # Mentorship views
│   ├── tests.py
│   │
│   ├── migrations/                    # Database migrations
│   │   └── __init__.py
│   │
│   └── templates/mentors/              # Mentor templates
│       ├── mentor_list.html           # List of mentors
│       ├── request_mentorship.html    # Request mentorship
│       ├── mentorship_requests.html   # View requests (mentor)
│       └── create_session.html        # Schedule session
│
├── hirehub/                           # Project Settings
│   ├── __init__.py
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL configuration
│   ├── wsgi.py                        # WSGI config
│   └── asgi.py                        # ASGI config
│
├── templates/                         # Base Templates
│   └── base.html                      # Base template with navbar
│
├── media/                            # User Uploads
│   └── resumes/                      # Resume files
│
├── staticfiles/                      # Collected static files (generated)
│   └── admin/                        # Admin static files
│
├── manage.py                         # Django management script
├── db.sqlite3                        # SQLite database (generated)
│
├── README.md                         # Project documentation
├── SETUP.md                          # Setup instructions
└── PROJECT_STRUCTURE.md              # This file
```
 
## Key Files Summary

### Models
- **accounts/models.py**: Profile model (User extension with role)
- **jobs/models.py**: Company, Job, JobApplication models
- **mentors/models.py**: MentorshipRequest, MentorSession models

### Views
- **accounts/views.py**: Authentication, dashboards, profile management
- **jobs/views.py**: Job CRUD, applications, company views
- **mentors/views.py**: Mentorship request handling

### Forms
- **accounts/forms.py**: UserRegistrationForm, ProfileUpdateForm
- **jobs/forms.py**: JobForm, JobApplicationForm, CompanyForm
- **mentors/forms.py**: MentorshipRequestForm, MentorSessionForm

### URLs
- **hirehub/urls.py**: Main URL configuration
- **accounts/urls.py**: Account-related URLs
- **jobs/urls.py**: Job-related URLs
- **mentors/urls.py**: Mentorship-related URLs

### Templates
- **templates/base.html**: Base template with Bootstrap 5
- **accounts/templates/accounts/**: 8 templates
- **jobs/templates/jobs/**: 10 templates
- **mentors/templates/mentors/**: 4 templates

### Admin
- **accounts/admin.py**: Profile admin
- **jobs/admin.py**: Company, Job, JobApplication admin
- **mentors/admin.py**: MentorshipRequest, MentorSession admin

### Utilities
- **accounts/decorators.py**: Role-based access decorators
- **accounts/signals.py**: Auto-create profile signals
- **jobs/management/commands/populate_companies.py**: Company data population

## File Count Summary

- **Python Files**: ~25 source files
- **HTML Templates**: 22 templates
- **Migrations**: Multiple migration files per app
- **Total Source Code**: ~3000+ lines

## Database Models

1. **Profile** (accounts) - User profiles with role-based fields
2. **Company** (jobs) - Company information
3. **Job** (jobs) - Job postings
4. **JobApplication** (jobs) - Job applications
5. **MentorshipRequest** (mentors) - Mentorship requests
6. **MentorSession** (mentors) - Scheduled sessions

## Features by File

### Authentication & Access
- `accounts/decorators.py` - Role-based access control
- `accounts/views.py` - Login, register, logout, dashboards
- `accounts/forms.py` - Registration forms

### Job Management
- `jobs/views.py` - Job CRUD, applications, filtering
- `jobs/forms.py` - Job creation/editing forms
- `jobs/models.py` - Job data models

### Mentorship
- `mentors/views.py` - Request handling, session scheduling
- `mentors/models.py` - Mentorship data models

### Data Population
- `jobs/management/commands/populate_companies.py` - Creates 100+ companies

---

**Note**: The `venv/` folder contains the virtual environment and is not part of the source code. It should be excluded when sharing the project.

