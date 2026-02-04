# How to Save/Backup Your HireHub Project

## Option 1: Create a ZIP Archive (Recommended)

### Using Windows File Explorer:
1. Right-click on the `Hirehub` folder
2. Select **"Send to"** → **"Compressed (zipped) folder"**
3. A ZIP file will be created (e.g., `Hirehub.zip`)
4. Move this ZIP to your desired location (USB, cloud storage, etc.)

### Using PowerShell:
```powershell
# Navigate to parent directory
cd C:\Users\User\OneDrive\Desktop

# Create ZIP file
Compress-Archive -Path Hirehub -DestinationPath Hirehub_backup.zip
```

---

## Option 2: Copy to Another Location

### Copy to USB Drive:
1. Insert USB drive
2. Copy the entire `Hirehub` folder
3. Paste it to your USB drive

### Copy to Another Folder:
```powershell
# Copy entire folder
Copy-Item -Path "C:\Users\User\OneDrive\Desktop\Hirehub" -Destination "D:\Backups\Hirehub" -Recurse
```

---

## Option 3: Use Git Version Control

### Initialize Git Repository:
```bash
cd C:\Users\User\OneDrive\Desktop\Hirehub

# Initialize git
git init

# Create .gitignore file (see below)
# Add files
git add .

# Commit
git commit -m "Initial commit - HireHub project"
```

### Create .gitignore file:
Create a file named `.gitignore` in the project root with:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
/media
/staticfiles

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### Push to GitHub/GitLab:
```bash
# Create repository on GitHub first, then:
git remote add origin https://github.com/yourusername/hirehub.git
git branch -M main
git push -u origin main
```

---

## Option 4: Cloud Storage Backup

### OneDrive (Already in OneDrive):
- Your project is already in OneDrive, so it's automatically synced
- Make sure OneDrive is running and synced

### Google Drive:
1. Install Google Drive desktop app
2. Copy `Hirehub` folder to Google Drive folder
3. It will sync automatically

### Dropbox:
1. Install Dropbox desktop app
2. Copy `Hirehub` folder to Dropbox folder
3. It will sync automatically

---

## Option 5: Create a Clean Backup (Exclude Unnecessary Files)

### What to EXCLUDE when backing up:
- `venv/` - Virtual environment (can be recreated)
- `__pycache__/` - Python cache files
- `db.sqlite3` - Database (can be regenerated)
- `staticfiles/` - Collected static files (can be regenerated)
- `*.pyc` - Compiled Python files

### What to INCLUDE:
- All `.py` files
- All `.html` templates
- `manage.py`
- `requirements.txt` (if you create one)
- `README.md`, `SETUP.md`, etc.
- `migrations/` folders

### Create requirements.txt:
```bash
# Generate requirements file
pip freeze > requirements.txt
```

### Clean Backup Script:
```powershell
# Create backup excluding unnecessary files
$exclude = @('venv', '__pycache__', '*.pyc', 'db.sqlite3', 'staticfiles')
$source = "C:\Users\User\OneDrive\Desktop\Hirehub"
$dest = "C:\Users\User\Desktop\Hirehub_Clean_Backup"

# Copy excluding specified items
robocopy $source $dest /E /XD venv __pycache__ staticfiles /XF db.sqlite3
```

---

## Option 6: Export as Complete Package

### Create a deployment package:
1. Create a new folder: `Hirehub_Package`
2. Copy all source files (exclude venv, db, cache)
3. Create `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
4. Create `INSTALL.txt` with setup instructions
5. ZIP the package

---

## Recommended Approach

**For College Project Submission:**

1. **Create a clean ZIP** excluding:
   - `venv/`
   - `__pycache__/`
   - `db.sqlite3`
   - `staticfiles/`

2. **Include these files:**
   - All source code (`.py` files)
   - All templates (`.html` files)
   - `manage.py`
   - `requirements.txt` (create it)
   - `README.md`
   - `SETUP.md`
   - `QUICK_START.md`

3. **Create requirements.txt:**
   ```bash
   pip freeze > requirements.txt
   ```

4. **ZIP the folder** and save to:
   - USB drive
   - Google Drive
   - Email to yourself
   - College submission portal

---

## Quick Save Commands

### Create ZIP Backup:
```powershell
cd C:\Users\User\OneDrive\Desktop
Compress-Archive -Path Hirehub -DestinationPath Hirehub_Backup_$(Get-Date -Format 'yyyy-MM-dd').zip
```

### Create Requirements File:
```bash
cd C:\Users\User\OneDrive\Desktop\Hirehub
.\venv\Scripts\Activate.ps1
pip freeze > requirements.txt
```

---

## File Size Considerations

- **Full folder**: ~500MB+ (includes venv)
- **Clean backup**: ~5-10MB (source code only)
- **ZIP file**: ~2-5MB (compressed)

**Recommendation**: Create a clean backup without `venv/` for sharing/submission.

---

## Restoring from Backup

1. Extract ZIP file
2. Create new virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   python manage.py populate_companies
   ```

---

**Your project is already saved in OneDrive!** But creating a backup ZIP is recommended for submission or sharing.

