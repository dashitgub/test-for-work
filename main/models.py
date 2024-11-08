from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_name

class Category(models.Model):  # связь Один ко многим с Product
    name = models.CharField(max_length=100)

class Product(models.Model):  # связи с Category и User
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Один ко многим
    users_favorites = models.ManyToManyField(User, related_name="favorite_products")  # Много ко многим

class Order(models.Model):  # связь Многие к одному с Product
    products = models.ManyToManyField(Product, related_name="orders")
    ordered_at = models.DateTimeField(auto_now_add=True)