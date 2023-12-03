from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('auth', views.auth, name='auth'),
    path('logout', views.logout_func, name='logout_func'),
]
