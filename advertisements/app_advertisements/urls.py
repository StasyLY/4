from django.urls import path
from . import views
urlpatterns = [
    path('', views.lesson4, name='lesson4'),
]