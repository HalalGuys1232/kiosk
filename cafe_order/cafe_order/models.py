
from django.db import models
# Create your models here.

class Category(models.Model): # Question
    name = models.CharField( max_length=100)
    def __str__(self):
        return self.name

class Item(models.Model): # Choice
    category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    item_name=models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now=True)
    item_count=models.IntegerField()
    order_price = models.IntegerField()
    def __str__(self):
        return self.item_count
