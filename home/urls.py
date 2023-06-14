from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home1/', views.home1_view, name='home1'),
]