from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone = forms.CharField(max_length=15, label='Phone Number')
    national_id = forms.CharField(max_length=20, label='National ID')
    county = forms.CharField(max_length=50, label='County of Residence')
    country = forms.CharField(max_length=50, label='Country of Residence')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.national_id = self.cleaned_data['national_id']
        user.county = self.cleaned_data['county']
        user.country = self.cleaned_data['country']
        user.save()
        return user
