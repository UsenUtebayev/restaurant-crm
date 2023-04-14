from django.urls import path

from landing.views import index, about

urlpatterns = [
    path('', index, name='landing'),
    path('about', about, name='about'),
]
