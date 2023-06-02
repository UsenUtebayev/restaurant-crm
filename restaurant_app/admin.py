from django.contrib import admin

from restaurant_app.models import Temperature, Humidity, Order, Instance, CornType


@admin.register(Temperature)
@admin.register(Humidity)
@admin.register(Order)
@admin.register(CornType)
@admin.register(Instance)
class AuthorAdmin(admin.ModelAdmin):
    pass
