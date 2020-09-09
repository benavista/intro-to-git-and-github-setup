from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfile
 
#Create your Form Here

class UserEntryForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    
    class Meta():
        model = User
        fields =('username','email','password')
        
class UserProfileForm(forms.ModelForm):
    
    class Meta():
        model = UserProfile
        fields =('Website','Profile_Pic') 
        