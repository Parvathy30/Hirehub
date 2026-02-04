# Quick Setup Guide

## Step-by-Step Setup Instructions

### 1. Activate Virtual Environment
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies (if not already installed)
```bash
pip install django
```

### 3. Run Migrations
```bash
# Create migrations for all apps
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

### 4. Populate Companies Database
```bash
python manage.py populate_companies
```
This will create 100+ companies in the database.

### 5. Create Superuser
```bash
python manage.py createsuperuser
```
Enter:
- Username: (your choice)
- Email: (optional)
- Password: (your choice)

### 6. Start Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
- **Home Page**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Testing the Application

### Test as Job Seeker:
1. Register at `/register/` with role "Job Seeker"
2. Login and complete profile
3. Browse jobs at `/jobs/`
4. Apply to a job
5. Check dashboard at `/seeker/dashboard/`

### Test as Job Provider:
1. Register at `/register/` with role "Job Provider"
2. Login and complete company profile
3. Post a job at `/provider/jobs/create/`
4. Go to admin panel and verify the job
5. View applicants in dashboard

### Test as Mentor:
1. Register at `/register/` with role "Mentor"
2. Login and complete profile (expertise, availability)
3. View requests in dashboard at `/mentor/dashboard/`

### Test Admin Features:
1. Login to admin panel
2. Verify jobs (make them visible)
3. Manage companies
4. View all users and applications

## Common Issues & Solutions

### Issue: "No module named 'django'"
**Solution**: Activate virtual environment and install Django:
```bash
pip install django
```

### Issue: "Profile matching query does not exist"
**Solution**: The signal should auto-create profiles. If not, run:
```bash
python manage.py shell
```
Then:
```python
from django.contrib.auth.models import User
from accounts.models import Profile
for user in User.objects.all():
    Profile.objects.get_or_create(user=user)
```

### Issue: Jobs not showing
**Solution**: Jobs need admin verification. Go to admin panel → Jobs → Select job → Check "Is verified" → Save

### Issue: Cannot see companies
**Solution**: Run the populate command:
```bash
python manage.py populate_companies
```

## Database Reset (if needed)

If you want to start fresh:
```bash
# Delete database
del db.sqlite3  # Windows
rm db.sqlite3    # Linux/Mac

# Recreate migrations
python manage.py makemigrations
python manage.py migrate

# Populate companies
python manage.py populate_companies

# Create superuser again
python manage.py createsuperuser
```

## Project Structure Overview

```
HireHub/
├── accounts/              # User management
│   ├── models.py         # Profile model
│   ├── views.py          # Auth & dashboard views
│   ├── forms.py          # Registration forms
│   ├── decorators.py     # Role-based access
│   └── signals.py        # Auto-create profiles
│
├── jobs/                 # Job management
│   ├── models.py        # Company, Job, JobApplication
│   ├── views.py         # Job CRUD & applications
│   ├── forms.py         # Job forms
│   └── management/      # Data population scripts
│
├── mentors/              # Mentorship
│   ├── models.py        # MentorshipRequest, MentorSession
│   ├── views.py         # Mentorship views
│   └── forms.py         # Mentorship forms
│
├── templates/            # Base templates
│   └── base.html        # Main layout
│
└── hirehub/             # Project settings
    ├── settings.py      # Django settings
    └── urls.py          # Main URL config
```

## Next Steps

1. ✅ Run migrations
2. ✅ Populate companies
3. ✅ Create superuser
4. ✅ Start server
5. ✅ Test all features
6. ✅ Verify jobs in admin
7. ✅ Test role-based access

## Support

For issues or questions, check:
- README.md for detailed documentation
- Django documentation: https://docs.djangoproject.com/
- Check console for error messages

---

**Happy Coding! 🚀**

