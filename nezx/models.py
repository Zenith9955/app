from django.db import models

# Create your models here.
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['CustomerName', 'Address', 'Agreement', 'AgreementDate', 'ExpireDate', 'OtherFiles']
