from django import forms
from .models import MentorshipRequest, MentorSession


class MentorshipRequestForm(forms.ModelForm):
    """Form for requesting mentorship"""
    class Meta:
        model = MentorshipRequest
        fields = ['mentor', 'message']
        widgets = {
            'mentor': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Why do you need mentorship? What are your goals?'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter to show only mentors
        from accounts.models import Profile
        self.fields['mentor'].queryset = Profile.objects.filter(role='mentor')


class MentorSessionForm(forms.ModelForm):
    """Form for scheduling mentorship sessions"""
    class Meta:
        model = MentorSession
        fields = ['session_time', 'topic', 'notes']
        widgets = {
            'session_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

