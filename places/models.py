from django.db import models
from authentication.models import User
from django.utils.timezone import localtime, timedelta


today = localtime().replace(hour=0, minute=0, second=0, microsecond=0)
tomorrow = localtime().replace(
    hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)


class Place(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='places'
    )
    name = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        upload_to='places/profile_pics/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @property
    def today_total(self):
        return sum(
            item.price for item in self.orders.filter(
                date__gte=today,
                date__lte=tomorrow,
                payed=True
            )
        )

    @property
    def total_to_charge(self):
        return sum(
            item.price for item in self.orders.filter(
                payed=False
            )
        )


class Table(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def getTotal(self):
        return sum(item.price for item in self.order_items.filter(payed=False))


class Item(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=True,
        related_name='orders'
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    payed = models.BooleanField(default=False)

    @property
    def price(self):
        return self.item.price * self.quantity
