# HireHub - Role-Based Job Portal

A comprehensive Django-based job portal with role-based access control for Job Seekers, Job Providers, and Mentors.

## Features

### 🔐 Authentication & User Management
- User registration with role selection (Seeker, Provider, Mentor)
- Login/Logout functionality
- Role-based dashboard redirection
- Profile management

### 👤 Job Seeker Features
- Browse verified job listings
- Filter jobs by company
- View job details
- Apply to jobs with resume upload
- Track application status
- View mentorship opportunities

### 🏢 Job Provider Features
- Create, edit, and delete job posts
- View applicants for each job
- Accept/reject applications
- Company management

### 🎓 Mentor Features
- View mentorship requests
- Accept/reject seekers
- Schedule mentorship sessions
- Manage mentorship relationships

### 🏭 Companies Module
- 100+ pre-populated companies
- Company listing and detail pages
- Jobs grouped under companies
- Company filtering

### 🔒 Access Control
- Role-based decorators
- Backend permission checks
- Unauthorized access handling

## Project Structure

```
HireHub/
├── accounts/          # User authentication & profiles
├── jobs/              # Job listings & applications
├── mentors/           # Mentorship functionality
├── hirehub/          # Project settings
├── templates/         # Base templates
├── media/            # User uploads (resumes)
└── manage.py
```

## Installation & Setup

### 1. Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### 2. Clone/Setup Project
```bash
# Navigate to project directory
cd HireHub

# Activate virtual environment (if using)
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Populate companies (100+ companies)
python manage.py populate_companies
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage Guide

### For Administrators
1. Access admin panel at `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Manage:
   - Users and Profiles
   - Companies
   - Jobs (verify/unverify)
   - Applications
   - Mentorship requests

### For Job Seekers
1. Register with role "Job Seeker"
2. Complete profile (skills, experience, resume)
3. Browse jobs at `/jobs/`
4. Apply to jobs
5. Track applications in dashboard
6. Request mentorship from mentors

### For Job Providers
1. Register with role "Job Provider"
2. Complete profile (company details)
3. Post jobs at `/provider/jobs/create/`
4. View applicants in dashboard
5. Accept/reject applications

### For Mentors
1. Register with role "Mentor"
2. Complete profile (expertise, availability)
3. View mentorship requests in dashboard
4. Accept/reject requests
5. Schedule sessions with accepted seekers

## Key URLs

- Home: `/`
- Register: `/register/`
- Login: `/login/`
- Jobs: `/jobs/`
- Companies: `/companies/`
- Seeker Dashboard: `/seeker/dashboard/`
- Provider Dashboard: `/provider/dashboard/`
- Mentor Dashboard: `/mentor/dashboard/`
- Admin: `/admin/`

## Models

### Accounts App
- **Profile**: User profile with role-based fields
- **User**: Django's built-in User model (extended)

### Jobs App
- **Company**: Company information
- **Job**: Job postings
- **JobApplication**: Job applications

### Mentors App
- **MentorshipRequest**: Mentorship requests
- **MentorSession**: Scheduled mentorship sessions

## Admin Features

The admin panel allows you to:
- Verify jobs (make them visible to seekers)
- Manage companies
- View all users and profiles
- Monitor applications
- Manage mentorship requests

## File Uploads

- Resumes are stored in `media/resumes/`
- Company logos in `media/company_logos/`
- Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured (already set)

## Security Features

- CSRF protection
- Role-based access control
- File upload validation
- SQL injection protection (Django ORM)
- XSS protection (Django templates)

## Troubleshooting

### Issue: Duplicate Profile Error
- Solution: The signals use `get_or_create()` to prevent duplicates. If you encounter this, delete the duplicate profile from admin.

### Issue: Jobs not showing
- Solution: Jobs need to be verified by admin. Go to admin panel and verify jobs.

### Issue: Cannot apply to jobs
- Solution: Ensure you're logged in as a Job Seeker role.

### Issue: Cannot post jobs
- Solution: Ensure you're logged in as a Job Provider role.

## Development Notes

- Uses SQLite by default (can be changed to PostgreSQL in settings.py)
- Bootstrap 5 for frontend styling
- Django 6.0
- All templates extend `base.html` for consistent UI

## Future Enhancements

- Email notifications
- Advanced search filters
- Resume parsing
- Interview scheduling
- Rating system
- Messaging system

## License

This is a college mini project for educational purposes.

## Author

HireHub Development Team

---

**Note**: This is a production-structured implementation suitable for college projects and viva presentations.

