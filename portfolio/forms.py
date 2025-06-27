from django import forms
from .models import CollaborationRequest

class CollaborationForm(forms.ModelForm):
    class Meta:
        model = CollaborationRequest
        fields = ['name', 'phone', 'email', 'gender', 'country', 'available_online', 'project_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'available_online': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project/Research Name'}),
        } 