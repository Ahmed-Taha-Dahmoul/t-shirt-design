from django.urls import path
from . import views

app_name = 'tshirtdesign'

urlpatterns = [
    path('create/', views.create, name='design_tshirt'),
    # Add more URL patterns for other views as needed
]