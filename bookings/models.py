from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    TABLE_SIZES = (
        (2, '2 seats'),
        (4, '4 seats'),
        (6, '6 seats'),
        (8, '8 seats'),
    )

    number = models.IntegerField(unique=True)
    size = models.IntegerField(choices=TABLE_SIZES)

    def __str__(self):
        return f"Table {self.number}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Reservation {self.id} by {self.user.username}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
