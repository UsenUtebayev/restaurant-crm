from django.contrib import admin

from restaurant_app.models import Food, Drink, Order, Client, Role, Booking, Place


@admin.register(Food)
@admin.register(Drink)
@admin.register(Order)
@admin.register(Client)
@admin.register(Role)
@admin.register(Booking)
@admin.register(Place)
class AuthorAdmin(admin.ModelAdmin):
    pass
