from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control'}))