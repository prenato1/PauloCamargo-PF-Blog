from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da página'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtítulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
