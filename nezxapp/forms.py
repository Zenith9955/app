# forms.py
from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    # Add more fields as needed
