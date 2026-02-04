from django import forms
from .models import Job, JobApplication, Company, JobReport


class JobForm(forms.ModelForm):
    """Form for creating/editing job posts"""
    class Meta:
        model = Job
        fields = ['company', 'title', 'description', 'skills_required', 'experience_required', 'location', 'salary', 'job_type']
        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Senior Software Engineer'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Describe the role, responsibilities, and benefits...'}),
            'skills_required': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Python, Django, JavaScript, SQL (comma-separated)'}),
            'experience_required': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2-3 years, Fresher'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Bangalore, Remote'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., ₹8-12 LPA, Negotiable'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'skills_required': 'Enter skills separated by commas for better skill matching',
        }


class JobApplicationForm(forms.ModelForm):
    """Form for job applications"""
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']
        widgets = {
            'resume': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us why you are a great fit for this role...'}),
        }


class CompanyForm(forms.ModelForm):
    """Form for creating/editing companies"""
    class Meta:
        model = Company
        fields = ['name', 'description', 'location', 'website', 'industry', 'founded_year', 'employee_count', 'logo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'founded_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'employee_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class JobReportForm(forms.ModelForm):
    """Form for reporting fake/fraudulent jobs"""
    class Meta:
        model = JobReport
        fields = ['reason', 'description']
        widgets = {
            'reason': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Please provide specific details about why you believe this job posting is suspicious or fraudulent...'
            }),
        }
        labels = {
            'reason': 'Reason for Report',
            'description': 'Detailed Description',
        }

