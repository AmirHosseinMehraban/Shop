from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    is_sub = models.BooleanField(default=False)
    sub_category = models.ManyToManyField('Category', related_name="scategory")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, related_name='pcategory')
    slug = models.SlugField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
