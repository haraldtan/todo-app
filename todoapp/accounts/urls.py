from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
]