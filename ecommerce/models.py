from django.db import models


CATEGORY_CHOICES = (
    ("Electronics", "Electronics"),
    ("Fashion", "Fashion"),
    ("Baby", "Baby"),
    ("Women", "Women"),
    ("M", "Men")
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    image = models.ImageField(upload_to="product_images", default="product.jpg")

    def __str__(self):
        return self.name