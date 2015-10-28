from django import forms
from django.contrib.auth.models import User
from farmstand.models import Product, UserProfile

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
        
class WeeklyProductForm(forms.ModelForm):


    product_list = tuple(
        [(id, name) for id, name in
            Product.objects.values_list('id', 'name')])

    selection = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=product_list)
    
    class Meta:
        model = Product
        exclude = ('quantity', 'unit', 'description', 'price')
        