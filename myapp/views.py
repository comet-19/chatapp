from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from myapp.forms import SignUpForm, CustomLoginForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import request
from django.contrib.auth import authenticate
from django.contrib import messages
from myapp.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LogoutView
from .forms import ChangeEmailForm

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
    
    
    def get_queryset(self):
        queryset = CustomUser.objects.exclude(id=self.request.user.id)
        return queryset
    

class Talk_RoomView(TemplateView):
    template_name = "myapp/talk_room.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friend_id = kwargs['friend_id']
        friend = CustomUser.objects.get(id=friend_id)
        context["friend"] = friend
        # context['friend_id'] = friend_id
        print(context)
        
        return context
    
        
class SettingView(TemplateView):
    template_name = "myapp/setting.html"
    
class ChangeUsernameView(UpdateView):
    model = CustomUser
    fields = ['username']
    template_name = 'myapp/change_username.html'
    success_url = reverse_lazy('setting')

    def get_object(self, queryset=None):
        # ログイン中のユーザーを取得して返す
        return self.request.user
    
class ChangeEmailView(UpdateView):
    model = CustomUser
    form_class = ChangeEmailForm
    template_name = 'myapp/change_email.html'
    success_url = reverse_lazy('setting')

    def get_object(self, queryset=None):
        return self.request.user
    
class ChangeIconView(UpdateView):
    model = CustomUser
    fields = ['image']
    template_name = 'myapp/change_icon.html'
    success_url = reverse_lazy('setting')
    
    def get_object(self, queryset=None):
        return self.request.user
    
class ChangePasswordView(PasswordChangeView):
    template_name = 'myapp/change_password.html'
    success_url = reverse_lazy('setting')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')
    
    

