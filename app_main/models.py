from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from app_users.models import Customer

class Product(models.Model):
    RATINGS_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to='product-images/', default='product-images/default.jpg')
    old_price = models.DecimalField(decimal_places=2, max_digits=10)
    new_price = models.DecimalField(decimal_places=2, max_digits=10)
    is_sale = models.BooleanField(default=True)
    rating = models.IntegerField(choices=RATINGS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.get_full_name()} - {self.body[:100]}"


class Cart(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        f"{self.owner} ning {self.product.name}"

    class Meta:
        unique_together = (
            ('owner', 'product'),
                           )