from django import forms

class CustomerForm(forms.Form):
    CustomerName = forms.CharField(label='Customer Name', max_length=100)
    Address = forms.CharField(label='Address', widget=forms.Textarea)
    Agreement = forms.FileField(label='Agreement', required=True)
    AgreementDate = forms.DateField(label='Agreement Date')
    ExpireDate = forms.DateField(label='Agreement Expire Date')
    OtherFiles = forms.FileField(label='Other Files', required=False)
