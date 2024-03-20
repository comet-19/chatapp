from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # 
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser  # CustomUserモデルを指定
        fields = ('username', 'email', 'password1', 'password2', 'image')  # 追加したフィールドを含める
    

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']

