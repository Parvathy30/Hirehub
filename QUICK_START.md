# Quick Start Guide - How to Run HireHub

## Step-by-Step Instructions

### 1. Open Terminal/Command Prompt
Navigate to the project directory:
```bash
cd C:\Users\User\OneDrive\Desktop\Hirehub
```

### 2. Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt.

### 3. Install Dependencies (if needed)
```bash
pip install django
```

### 4. Run Database Migrations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

### 5. Populate Companies Database
```bash
python manage.py populate_companies
```
This creates 100+ companies in the database.

### 6. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Enter:
- Username: (choose any username, e.g., "admin")
- Email: (optional, press Enter to skip)
- Password: (choose a password)
- Password confirmation: (enter same password)

### 7. Start the Development Server
```bash
python manage.py runserver
```

### 8. Access the Application

Open your web browser and go to:

- **Home Page**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## Complete Command Sequence (Copy & Paste)

```bash
# 1. Navigate to project (if not already there)
cd C:\Users\User\OneDrive\Desktop\Hirehub

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Populate companies
python manage.py populate_companies

# 5. Create superuser (follow prompts)
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

---

## Testing the Application

### Test as Job Seeker:
1. Go to http://127.0.0.1:8000/register/
2. Register with role "Job Seeker"
3. Login and complete your profile
4. Browse jobs at http://127.0.0.1:8000/jobs/
5. Apply to a job
6. Check dashboard at http://127.0.0.1:8000/seeker/dashboard/

### Test as Job Provider:
1. Register with role "Job Provider"
2. Login and complete company profile
3. Post a job at http://127.0.0.1:8000/provider/jobs/create/
4. Go to admin panel and verify the job (check "Is verified")
5. View applicants in dashboard

### Test as Mentor:
1. Register with role "Mentor"
2. Login and complete profile (expertise, availability)
3. View requests in dashboard

### Test Admin Features:
1. Login to http://127.0.0.1:8000/admin/
2. Verify jobs (make them visible to seekers)
3. Manage companies and users

---

## Troubleshooting

### Issue: "No module named 'django'"
**Solution**: Activate virtual environment and install Django:
```bash
.\venv\Scripts\Activate.ps1
pip install django
```

### Issue: "Profile matching query does not exist"
**Solution**: The signal should auto-create profiles. If not, run:
```bash
python manage.py shell
```
Then in Python shell:
```python
from django.contrib.auth.models import User
from accounts.models import Profile
for user in User.objects.all():
    Profile.objects.get_or_create(user=user)
exit()
```

### Issue: Jobs not showing
**Solution**: Jobs need admin verification:
1. Go to admin panel → Jobs
2. Select a job
3. Check "Is verified" checkbox
4. Save

### Issue: Cannot see companies
**Solution**: Run the populate command:
```bash
python manage.py populate_companies
```

### Issue: Port already in use
**Solution**: Use a different port:
```bash
python manage.py runserver 8001
```

---

## Important URLs

- Home: `/`
- Register: `/register/`
- Login: `/login/`
- Jobs: `/jobs/`
- Companies: `/companies/`
- Seeker Dashboard: `/seeker/dashboard/`
- Provider Dashboard: `/provider/dashboard/`
- Mentor Dashboard: `/mentor/dashboard/`
- Admin: `/admin/`

---

## First Time Setup Checklist

- [ ] Virtual environment activated
- [ ] Django installed
- [ ] Migrations created and applied
- [ ] Companies populated (100+)
- [ ] Superuser created
- [ ] Server running
- [ ] Can access home page
- [ ] Can login to admin panel

---

**That's it! Your HireHub application is now running! 🚀**

