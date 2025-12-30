from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'file']
        labels = {
            'title': 'Document Title',
            'description': 'Short Description',
            'file': 'Upload File'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter document title',
                'class': 'input_field'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter a short description',
                'rows': 4,
                'class': 'edit_desc_area'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'edit_file_upload'
            })
        }