from django.urls import path
from . import views
from .views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('friends', views.FriendsView.as_view(), name='friends'),
    path('talk_room/<int:friend_id>/', views.Talk_RoomView.as_view(), name='talk_room'),
    path('setting', views.SettingView.as_view(), name='setting'),
    path('setting/change_username', views.ChangeUsernameView.as_view(), name='change_username'),
    path('setting/change_email', views.ChangeEmailView.as_view(), name='change_email'),
    path('setting/change_icon', views.ChangeIconView.as_view(), name='change_icon'),
    path('setting/change_password', views.ChangePasswordView.as_view(), name='change_password'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
