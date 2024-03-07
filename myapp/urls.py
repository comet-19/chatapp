from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('friends', views.FriendsView.as_view(), name='friends'),
    path('talk_room', views.Talk_RoomView.as_view(), name='talk_room'),
    path('setting', views.SettingView.as_view(), name='setting'),
]
