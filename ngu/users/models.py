from django.db import models
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img = models.ImageField(default="default.jpg",upload_to="profile")
    def __str__(self):
        return f'{self.user.username} Profile'
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields ={
            
            
            'email',
            'last_name',
            'first_name',
            
        }
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=('user',)


