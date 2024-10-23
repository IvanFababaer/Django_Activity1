from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app2-home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
]