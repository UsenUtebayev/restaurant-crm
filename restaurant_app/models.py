import math

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class Client(User):
    role = models.ForeignKey("Role", on_delete=models.CASCADE, related_name="role")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Клиент"


class Role(models.Model):
    title = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.title


class Drink(models.Model):
    title = models.CharField(max_length=248)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(max_length=4096, blank=True)

    def __str__(self):
        return f"{self.title}, бағасы: {str(self.price)} тг"


class Food(models.Model):
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(max_length=4096, blank=True)
    cook_time = models.IntegerField()

    def __str__(self):
        return f"{self.title}, бағасы: {str(self.price)} тг, әзірлеу уақыты: {str(math.floor(self.cook_time / 60))} мин"


class Order(models.Model):
    client = ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    food = ForeignKey("Food", on_delete=models.CASCADE, related_name="food_order")
    drink = ForeignKey("Drink", on_delete=models.CASCADE, related_name="drink_order")
    description = models.TextField(blank=True, max_length=4096)
    order_time = models.DateTimeField(auto_now_add=True)
    waiter = ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='waiter')
    cook = ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='cook', blank=True)

    def __str__(self):
        return str(self.client) + " " + str(self.order_time) + " " + str(self.waiter) + " " + str(self.cook)


class Booking(models.Model):
    client = ForeignKey(Client, on_delete=models.CASCADE)
    taking_place = ForeignKey('Place', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Клиент:{self.client.username}, орны:{self.taking_place_id}, Дата брони:{self.created_at}"


class Place(models.Model):
    is_vip = models.BooleanField(blank=True, null=True)
    is_engaged = models.BooleanField(default=False)
    is_for_children = models.BooleanField(default=False)

    def __str__(self):
        vip = "VIP" if self.is_vip else ""
        for_children = 'для детей' if self.is_for_children else "для взрослых"
        return f"{vip} Орын:{self.pk}, {for_children}"
