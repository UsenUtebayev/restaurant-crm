import math

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey


class Equipment(models.Model):
    name = models.CharField(max_length=128)
    serial_key = models.CharField(max_length=128)

    def __str__(self):
        return f'Название аппарата: {self.name}, серийный номер: {self.serial_key}'

class Temperature(models.Model):
    title = models.CharField(max_length=248)
    description = models.TextField(max_length=4096, blank=True)

    def __str__(self):
        return f"{self.title}"


class Humidity(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=4096, blank=True)
    cook_time = models.IntegerField()

    def __str__(self):
        return f"{self.title} время процесса: {str(math.floor(self.cook_time / 60))} мин"


class CornType(models.Model):
    type = models.CharField(max_length=128)
    grade = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])

    def __str__(self):
        return f"Тип зерна: {self.type}, сорт: {self.grade}"


class Instance(models.Model):
    weight = models.IntegerField()
    type = models.ForeignKey(CornType, related_name="corn_type", on_delete=models.CASCADE)

    def __str__(self):
        return f'Номер партий:{self.pk}, вес: {self.weight / 1000} тонн, тип: {self.type.type}' \
               f', сорт: {self.type.grade}'


class Order(models.Model):
    client = ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    humidity = ForeignKey(Humidity, on_delete=models.CASCADE, related_name="humidity")
    temperature = ForeignKey(Temperature, on_delete=models.CASCADE, related_name="temperature")
    description = models.TextField(blank=True, max_length=4096)
    order_time = models.DateTimeField(auto_now_add=True)
    instance = ForeignKey(Instance, related_name='instance', on_delete=models.CASCADE)
    equipment = ForeignKey(Equipment, related_name='equipment', on_delete=models.CASCADE)

    def __str__(self):
        return f'Пользватель:{self.client}, {self.humidity}, {self.temperature}, {self.order_time.strftime("%Y-%m-%d %H:%M")},' \
               f' {self.instance}'
