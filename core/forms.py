from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'contact-input'}),
            'last_name': forms.TextInput(attrs={'class': 'contact-input1'}),
            'email': forms.EmailInput(attrs={'class': 'contact-input2'}),
            'position': forms.TextInput(attrs={'class': 'contact-input2'}),
            'company': forms.TextInput(attrs={'class': 'contact-input2'}),
            'country': forms.TextInput(attrs={'class': 'contact-input2'}),
            'message': forms.Textarea(attrs={'class': 'contact-text'}),
        }

 