from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import SignUpForm, CustomLoginForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import request
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    template_name = 'myapp/index.html'

class SignupView(CreateView):
    template_name = "myapp/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")
        
    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'myapp/login.html'
    

class FriendsView(ListView):
    model = CustomUser
    context_object_name = 'friends'
    template_name = "myapp/friends.html"

class Talk_RoomView(TemplateView):
    template_name = "myapp/talk_room.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friend_id = kwargs['friend_id']
        context['friend_id'] = friend_id 
        return context
    
        
class SettingView(TemplateView):
    template_name = "myapp/setting.html"
