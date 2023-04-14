from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order', include('restaurant_app.urls')),
    path('', include('landing.urls')),
]
