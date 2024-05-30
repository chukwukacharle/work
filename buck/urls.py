from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='buck-home'),
    path('about/', views.about, name='buck-about'),
    ]
