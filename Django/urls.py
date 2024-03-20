from django.contrib import admin
from django.urls import include, path
from RegnvaktenApp import views as regnvakten_views

urlpatterns = [
    path('', regnvakten_views.weather_view, name='home'),
    path("weather/", include("RegnvaktenApp.urls")),
    path('admin/', admin.site.urls)
]
