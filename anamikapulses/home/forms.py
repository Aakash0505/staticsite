from django import forms
from .models import Contact, AreaOfInterest
from django_recaptcha import fields
from django_recaptcha import widgets
from django.core import validators
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class CaptchaForm(forms.Form):

    captcha = fields.ReCaptchaField(
        widget=widgets.ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'light',
                'data-size': 'normal',
            })
    )



class FormContactusView(CaptchaForm,forms.ModelForm):
    area_of_interest = forms.ModelChoiceField(
        queryset=AreaOfInterest.objects.filter(published=True),  # Filter by published job openings
        empty_label="Select Area of Interest",  # Default label for the dropdown
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'your-sud'})  # Add form-control class and id for styling
    )

    class Meta:
        model = Contact
        fields = ('name', 'email_id', 'contact_no','area_of_interest', 'message', 'document', 'captcha')