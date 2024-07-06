from django.contrib import admin
from django.urls import path
from EDapp import views
urlpatterns = [
    path("", views.Login, name="Login"),
    path("login", views.Login, name='login'),
    path("userlogout", views.userlogout, name='logout'),
    path("home", views.home, name="home"),
    path("encoder", views.encoder, name="encoder"),
    path("decoder", views.decoder, name="decoder")
]

