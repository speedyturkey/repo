from django import forms
from django.contrib.auth.models import User
from farmstand.models import Products, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('street_address1',
                   'street_address2',
                   'city',
                   'state'
        )