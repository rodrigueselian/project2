from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f" {self.id}, {self.category}"

class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    item = models.CharField(max_length=64)
    price = models.IntegerField()
    description = models.TextField()
    active = models.BooleanField(default=True)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    selectcategory = models.ManyToManyField(Category, blank=True, related_name="category_items")

    def __str__(self):
        return f"{self.seller}, {self.item}, {self.description}, {self.active}, {self.price}"

class Bid(models.Model):
    item_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_bids")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comprador")
    bid = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer}, bid {self.bid}, {self.date}"

class Comment(models.Model):
    item_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user},  {self.comment}, {self.item_id}"

class Watchlist(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_watchlist")
    item_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_watchlist")

    def __str__(self):
        return f"{self.usuario}, {self.item_id}, {self.id}"