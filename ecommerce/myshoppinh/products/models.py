from django.db import models
from base.model import baseModel

class category(baseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

class product(baseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField()
    product_description = models.CharField(max_length=255)  # You must specify max_length

class productImage(baseModel):
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(upload_to="product")
