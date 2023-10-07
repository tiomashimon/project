from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'phone_number', 'message')