from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    is_sub = models.BooleanField(default=False)
    sub_category = models.ForeignKey('Category', on_delete=models.CASCADE ,related_name="scategory", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pcategory')
    slug = models.SlugField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    modals = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)
    star = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
