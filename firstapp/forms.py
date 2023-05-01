from users.models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
designation = (
    ("Web Developer", "Web Developer"),
    ("Web Designer", "Web Designer"),
    ("Graphic Designer", "Graphic Designer"),
    ("Digital Marketing", "Digital Marketing"),

)
role = (
    ("Admin", "Admin"),
    ("User", "User"),
    ("H R", "H R"),
    ("Designer", "Designer"),

)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('profile', 'email',)
        

class UserUpdateForm(forms.ModelForm):
    designation=forms.ChoiceField(choices=designation, widget=forms.Select(attrs={'class': 'form-control'}))
    role=forms.ChoiceField(choices=role, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = MyUser
        fields = ['profile', 'email','name','designation','role']
        
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('email', 'name', 'image', 'phone')